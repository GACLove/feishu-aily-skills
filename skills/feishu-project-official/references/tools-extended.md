# 扩展工具索引

以下工具按需使用，不属于核心流程但覆盖常见操作。所有工具均需传入 `project_key`（除非标注可选）。

## 查询类

| 意图 | 工具 | 关键必填参数 |
|------|------|-------------|
| 查询可流转状态 | `get_transitable_states` | project_key, work_item_id, work_item_type, user_key |
| 查询流转必填项 | `get_transition_required` | project_key, work_item_id, state_key |
| 搜索视图 | `search_view_by_title` | project_key, view_scope, key_word |
| 查询团队列表 | `list_project_team` | project_key（可选） |
| 查询团队成员 | `list_team_members` | project_key, team_id |
| 查询评论 | `list_workitem_comments` | project_key, work_item_id |
| 查询操作记录 | `get_workitem_op_record` | project_key, work_item_id |
| 查询工时记录 | `get_workitem_man_hour_records` | project_key, work_item_type, work_item_id |
| 查询关联工作项 | `list_related_workitems` | project_key, work_item_type, work_item_id, relation_work_item_type_key, relation_key |
| 查询关联关系定义 | `list_workitem_relations` | project_key |
| 查询图表列表 | `list_charts` | project_key, view_id |
| 查询图表详情 | `get_chart_detail` | chart_id |
| 查询节点字段配置 | `list_node_field_config` | project_key, work_item_type |
| 获取创建元信息 | `get_workitem_field_meta` | project_key |

## 操作类

| 意图 | 工具 | 关键必填参数 | 说明 |
|------|------|-------------|------|
| 修改节点 | `update_node` | work_item_id, node_id | 修改节点排期、负责人、自定义字段。排期/差异化排期/负责人不要同时修改 |
| 子任务操作 | `update_node_subtask` | node_id, work_item_id, action | action: create/update/confirm/rollback |
| 添加评论 | `add_comment` | work_item_id, comment_content | 支持 markdown |
| 创建固定视图 | `create_fixed_view` | project_key, name, work_item_type, work_item_id_list | 上限 200 个工作项 |
| 更新固定视图 | `update_fixed_view` | project_key, view_id, work_item_type | add/remove_work_item_ids 二选一 |

## 补充错误速查

以下为低频但需注意的错误场景（高频错误见 SKILL.md）：

| 错误现象 | 原因 | 修复方式 |
|---------|------|---------|
| MQL 返回为空但数据存在 | 字段名用了英文 field_key | 调用 `list_workitem_field_config` 确认字段名 |
| 日期区间字段查询失败 | 直接查询了区间字段 | 用子字段 `` `__字段名_开始时间` `` |
| 角色查询无结果 | 未加 `__` 前缀 | 用 `` `__{角色名}` `` 格式 |
| 空间名不唯一 | 中文名匹配到多个空间 | 用 `search_project_info` 验证后用 project_key 重新调用 |
| 人员字段写入失败 | field_value 格式不对 | user 类型传单个 userkey，multi-user 传 userkey 数组 |
| 字段名不正确 | 字段 key 拼写错误 | 先 `list_workitem_field_config` 确认 |
