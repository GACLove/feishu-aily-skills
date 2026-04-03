#!/usr/bin/env python3
"""Skill-checker scoring utilities.

All commands read JSON from stdin (or an optional file arg) and write to stdout.
No intermediate files — agent pipes data through these commands.

Commands:
    eval-summary    Count pass/fail, compute pass_rate
    env-summary     Count compatibility categories, compute fitness_score
    merge           Combine all dimensions into a single check.json
    split           Stratified train/test split
"""

import argparse
import json
import random
import sys
from datetime import datetime, timezone


def _read(path=None):
    if path and path != "-":
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def _out(data):
    json.dump(data, sys.stdout, indent=2, ensure_ascii=False)
    print()


# ── eval-summary ─────────────────────────────────────────

def eval_summary(items, skill_name="", description=""):
    results = []
    for item in items:
        passed = item["triggered"] == item["should_trigger"]
        results.append({
            "query": item["query"],
            "should_trigger": item["should_trigger"],
            "triggered": item["triggered"],
            "pass": passed,
        })
    n_passed = sum(1 for r in results if r["pass"])
    total = len(results)
    return {
        "skill_name": skill_name,
        "description": description,
        "results": results,
        "summary": {
            "total": total,
            "passed": n_passed,
            "failed": total - n_passed,
            "pass_rate": round(n_passed / total, 4) if total else 0,
        },
    }


# ── env-summary ──────────────────────────────────────────

def env_summary(dependencies):
    counts = {"compatible": 0, "adaptable": 0, "incompatible": 0, "unknown": 0}
    blocking, adaptations = [], []
    for dep in dependencies:
        c = dep.get("compatibility", "unknown")
        counts[c] = counts.get(c, 0) + 1
        if c == "incompatible":
            blocking.append(dep.get("name", ""))
        elif c == "adaptable":
            adaptations.append(dep.get("name", ""))
    total = len(dependencies)
    ok = counts["compatible"] + counts["adaptable"]
    return {
        "total": total,
        **counts,
        "blocking_issues": blocking,
        "adaptations_available": adaptations,
        "fitness_score": round(ok / total, 4) if total else 1.0,
    }


# ── merge ────────────────────────────────────────────────

def merge(skill_name, trigger=None, environment=None, evals=None,
          optimization=None):
    """Combine all dimensions into a single check.json report."""
    dims = {}

    if trigger is not None:
        s = trigger.get("summary", {})
        dims["trigger"] = {
            "status": "checked",
            "score": s.get("pass_rate", 0),
            "results": trigger.get("results", []),
            "summary": s,
            "description_used": trigger.get("description", ""),
        }
    else:
        dims["trigger"] = {"status": "skipped"}

    if environment is not None:
        s = environment.get("summary", {})
        dims["environment"] = {
            "status": "checked",
            "score": s.get("fitness_score", 0),
            "dependencies": environment.get("dependencies", []),
            "summary": s,
        }
    else:
        dims["environment"] = {"status": "skipped"}

    checked = [d for d in dims.values() if d["status"] == "checked"]
    overall = (round(sum(d["score"] for d in checked) / len(checked), 4)
               if checked else 0)

    report = {
        "skill_name": skill_name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "overall_score": overall,
        "dimensions": dims,
    }
    if evals is not None:
        report["evals"] = evals
    if optimization is not None:
        report["optimization"] = optimization
    return report


# ── split ────────────────────────────────────────────────

def split_eval_set(eval_set, holdout=0.4, seed=42):
    random.seed(seed)
    pos = [e for e in eval_set if e["should_trigger"]]
    neg = [e for e in eval_set if not e["should_trigger"]]
    random.shuffle(pos)
    random.shuffle(neg)
    np = max(1, int(len(pos) * holdout))
    nn = max(1, int(len(neg) * holdout))
    return {
        "train": pos[np:] + neg[nn:],
        "test": pos[:np] + neg[:nn],
    }


# ── CLI ──────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="Skill-checker scoring")
    sub = p.add_subparsers(dest="cmd")

    s1 = sub.add_parser("eval-summary")
    s1.add_argument("input", nargs="?", help="JSON file (default: stdin)")
    s1.add_argument("--skill-name", default="")
    s1.add_argument("--description", default="")

    s2 = sub.add_parser("env-summary")
    s2.add_argument("input", nargs="?")

    s3 = sub.add_parser("merge")
    s3.add_argument("input", nargs="?", help="JSON: {skill_name, trigger, environment, evals, ...}")
    s3.add_argument("--skill-name", default="")

    s4 = sub.add_parser("split")
    s4.add_argument("input", nargs="?")
    s4.add_argument("--holdout", type=float, default=0.4)
    s4.add_argument("--seed", type=int, default=42)

    args = p.parse_args()

    if args.cmd == "eval-summary":
        _out(eval_summary(_read(args.input), args.skill_name, args.description))

    elif args.cmd == "env-summary":
        data = _read(args.input)
        deps = data.get("dependencies", data) if isinstance(data, dict) else data
        summary = env_summary(deps)
        if isinstance(data, dict) and "dependencies" in data:
            data["summary"] = summary
            _out(data)
        else:
            _out(summary)

    elif args.cmd == "merge":
        data = _read(args.input)
        _out(merge(
            skill_name=args.skill_name or data.get("skill_name", ""),
            trigger=data.get("trigger"),
            environment=data.get("environment"),
            evals=data.get("evals"),
            optimization=data.get("optimization"),
        ))

    elif args.cmd == "split":
        _out(split_eval_set(_read(args.input), args.holdout, args.seed))

    else:
        p.print_help()


if __name__ == "__main__":
    main()
