# 缓存文件格式

所有缓存文件使用 markdown，方便直接阅读和编辑。

## groups.md

markdown 表格，每行一个群组：

```markdown
# 关注的群组

| 群名 | chat_id | 备注 |
|------|---------|------|
| 群名称 | oc_xxx | 用途简述 |
```

- `chat_id` 用于调用 `aily-im list-messages`
- `备注` 可为空，由 agent 在了解群用途后补充

## contacts.md

markdown 表格，每行一个联系人：

```markdown
# 联系人

| 姓名 | user_id | 角色 | 备注 |
|------|---------|------|------|
| 张三 | ou_xxx | 产品经理 | 负责XX项目 |
```

- `user_id` 可为空（从消息中发现但尚未查询 ID 的联系人）
- `角色` 和 `备注` 由 agent 在交互中逐步补充

## daily/YYYY-MM-DD.md

每日消息快照，按群组分节：

```markdown
# YYYY-MM-DD 消息快照

## 群名 (chat_id)

[HH:MM] 发送者: 消息内容
[HH:MM] 发送者: 消息内容
...
```

- 直接使用 `aily-im list-messages` 输出的 `.md` 内容
- 保留 7 天，由定时任务自动清理

## summary.md

活跃群和近期要点汇总：

```markdown
# 飞书上下文摘要

最后更新: YYYY-MM-DD

## 活跃群组
- 群名: 今日 N 条消息，主要讨论XXX

## 近期要点
- 要点1
- 要点2
```

- 由定时任务自动更新活跃群组部分
- 可在交互中补充近期要点