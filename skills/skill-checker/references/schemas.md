# JSON Schemas

所有数据在内存中流转，仅产出一个文件：`{skill_name}.check.json`。

---

## check.json — 唯一产出文件

包含测试集、触发评测、环境扫描、优化记录的完整数据。

```json
{
  "skill_name": "my-skill",
  "timestamp": "2026-03-07T12:00:00+00:00",
  "overall_score": 0.85,
  "evals": [
    {"query": "帮我检查这个 skill", "should_trigger": true},
    {"query": "帮我写一个新 skill", "should_trigger": false}
  ],
  "dimensions": {
    "trigger": {
      "status": "checked",
      "score": 0.9,
      "description_used": "Use this skill when...",
      "results": [
        {"query": "...", "should_trigger": true, "triggered": true, "pass": true}
      ],
      "summary": {"total": 20, "passed": 18, "failed": 2, "pass_rate": 0.9}
    },
    "environment": {
      "status": "checked",
      "score": 0.875,
      "dependencies": [
        {
          "category": "tool",
          "name": "bash",
          "description": "what the skill needs",
          "evidence": "quote from SKILL.md",
          "compatibility": "compatible",
          "reason": "why"
        },
        {
          "category": "capability",
          "name": "user_choices",
          "description": "Presents options to user",
          "evidence": "Step 3: Present 3-5 options",
          "compatibility": "adaptable",
          "reason": "Has structured clarification",
          "adaptation": {
            "target_capability": "clarification tool",
            "strategy": "replace",
            "description": "Use clarification tool instead of text",
            "changes": ["Replace text-based option listing with clarification tool"]
          }
        }
      ],
      "summary": {
        "total": 8, "compatible": 5, "adaptable": 1, "incompatible": 1, "unknown": 1,
        "blocking_issues": ["anthropic_sdk"],
        "adaptations_available": ["user_choices"],
        "fitness_score": 0.75
      }
    }
  },
  "optimization": {
    "iterations": [
      {"iteration": 1, "description": "...", "train_passed": 10, "train_total": 12}
    ],
    "best": {"description": "...", "test_score": 0.95}
  }
}
```

### 顶层字段

| Field | Type | Description |
|-------|------|-------------|
| `skill_name` | string | Skill 名称 |
| `timestamp` | string | ISO 8601 UTC |
| `overall_score` | float | 各维度均分 (0.0–1.0) |
| `evals` | object[] | 测试集（query + should_trigger） |
| `dimensions.trigger` | object | 触发评测维度 |
| `dimensions.environment` | object | 环境扫描维度 |
| `optimization` | object | 优化迭代记录（可选，仅优化时产出） |

### trigger 维度

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | `"checked"` or `"skipped"` |
| `score` | float | pass_rate |
| `description_used` | string | 被测试的 description |
| `results[]` | object[] | 每条 query 的 triggered/pass 结果 |
| `summary` | object | total, passed, failed, pass_rate |

### environment 维度

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | `"checked"` or `"skipped"` |
| `score` | float | fitness_score |
| `dependencies[]` | object[] | 依赖项列表 |
| `summary` | object | 分类计数 + fitness_score |

### dependency 对象

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `category` | string | yes | `tool` / `capability` / `external_service` / `implicit` |
| `name` | string | yes | 短标识符（也用于 frontmatter dependencies） |
| `description` | string | yes | 需要什么、为什么 |
| `evidence` | string | yes | SKILL.md 原文引用 |
| `compatibility` | string | yes | `compatible` / `adaptable` / `incompatible` / `unknown` |
| `reason` | string | yes | 分类理由 |
| `adaptation` | object | no | 适配方案（adaptable 项） |
| `adaptation.target_capability` | string | yes* | 替代能力 |
| `adaptation.strategy` | string | yes* | `replace` / `wrap` / `degrade` / `remove` |
| `adaptation.description` | string | yes* | 改什么、为什么 |
| `adaptation.changes` | string[] | yes* | 具体的 SKILL.md 修改 |

\* Required when `adaptation` is present.

### optimization 对象

| Field | Type | Description |
|-------|------|-------------|
| `iterations[]` | object[] | 每轮记录：iteration, description, train_passed, train_total |
| `best.description` | string | 最优 description |
| `best.test_score` | float | test set 最终得分 |
