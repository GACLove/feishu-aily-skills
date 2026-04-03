# MCP 工具调用示例

所有示例均通过 `aily-mcp call -s ms_official_meego -t <工具名> -p '<JSON参数>'` 格式调用。

---

## 元数据查询

### search_project_info

```bash
aily-mcp call -s ms_official_meego -t search_project_info -p '{"project_key": "空间名或key"}'
```

### list_workitem_types

```bash
aily-mcp call -s ms_official_meego -t list_workitem_types -p '{"project_key": "空间key"}'
```

### list_workitem_field_config

```bash
# 查询所有字段
aily-mcp call -s ms_official_meego -t list_workitem_field_config -p '{"project_key": "空间key", "work_item_type": "story", "page_num": 1}'

# 精确查询模板字段
aily-mcp call -s ms_official_meego -t list_workitem_field_config -p '{"project_key": "空间key", "work_item_type": "story", "page_num": 1, "field_keys": ["template"]}'
```

### list_workitem_role_config

```bash
aily-mcp call -s ms_official_meego -t list_workitem_role_config -p '{"project_key": "空间key", "work_item_type": "story", "page_num": 1}'
```

### search_user_info

```bash
aily-mcp call -s ms_official_meego -t search_user_info -p '{"user_keys": ["张三", "李四"]}'
```

---

## 数据查询

### search_by_mql

```bash
# 查询空间中所有未冻结的需求
aily-mcp call -s ms_official_meego -t search_by_mql -p '{"project_key": "空间key", "mql": "SELECT `work_item_id`, `name`, `current_owners`, `status` FROM `空间名`.`story` WHERE `is_archived` = 0"}'

# 查询本周创建的需求
aily-mcp call -s ms_official_meego -t search_by_mql -p '{"project_key": "空间key", "mql": "SELECT `work_item_id`, `name` FROM `空间名`.`story` WHERE RELATIVE_DATETIME_EQ(`created_at`, '\''current_week'\'')"}'

# 查询指派给当前登录用户且未完成的需求
aily-mcp call -s ms_official_meego -t search_by_mql -p '{"project_key": "空间key", "mql": "SELECT `work_item_id`, `name`, `status` FROM `空间名`.`story` WHERE array_contains(`current_owners`, current_login_user()) AND `is_archived` = 0"}'

# 查询某团队负责的需求
aily-mcp call -s ms_official_meego -t search_by_mql -p '{"project_key": "空间key", "mql": "SELECT `work_item_id`, `name` FROM `空间名`.`story` WHERE any_match(`current_owners`, x -> x in team(true, '\''后端开发团队'\''))"}'
```

### get_workitem_brief

```bash
aily-mcp call -s ms_official_meego -t get_workitem_brief -p '{"work_item_id": "工作项ID或名称", "project_key": "空间key"}'
```

### list_todo

```bash
# 查询我的待办
aily-mcp call -s ms_official_meego -t list_todo -p '{"action": "todo", "page_num": 1}'

# 查询逾期事项
aily-mcp call -s ms_official_meego -t list_todo -p '{"action": "overdue", "page_num": 1}'
```

### list_schedule

```bash
aily-mcp call -s ms_official_meego -t list_schedule -p '{"project_key": "空间key", "user_keys": ["张三", "李四"], "work_item_type_keys": ["story", "sub_task"], "start_time": "2025-03-01", "end_time": "2025-03-31"}'
```

### get_view_detail

```bash
aily-mcp call -s ms_official_meego -t get_view_detail -p '{"view_id": "视图ID", "project_key": "空间key"}'
```

### get_node_detail

```bash
aily-mcp call -s ms_official_meego -t get_node_detail -p '{"work_item_id": "工作项ID", "node_id_list": ["节点ID或_all"], "project_key": "空间key"}'
```

---

## 数据操作

### create_workitem

```bash
aily-mcp call -s ms_official_meego -t create_workitem -p '{
  "project_key": "空间key",
  "work_item_type": "story",
  "fields": [
    {"field_key": "template", "field_value": "模板ID"},
    {"field_key": "name", "field_value": "需求标题"},
    {"field_key": "priority", "field_value": "option_id"}
  ]
}'
```

### update_field

```bash
# 更新普通字段
aily-mcp call -s ms_official_meego -t update_field -p '{
  "work_item_id": "工作项ID",
  "project_key": "空间key",
  "fields": [
    {"field_key": "priority", "field_value": "option_id"}
  ]
}'

# 更新角色
aily-mcp call -s ms_official_meego -t update_field -p '{
  "work_item_id": "工作项ID",
  "project_key": "空间key",
  "role_operate": [
    {"op": "add", "role_key": "RD", "user_keys": ["userkey1"]}
  ]
}'
```

### transition_node

```bash
# 完成节点
aily-mcp call -s ms_official_meego -t transition_node -p '{"work_item_id": "工作项ID", "node_id": "节点ID", "action": "confirm", "project_key": "空间key"}'

# 回滚节点
aily-mcp call -s ms_official_meego -t transition_node -p '{"work_item_id": "工作项ID", "node_id": "节点ID", "action": "rollback", "rollback_reason": "回滚原因", "project_key": "空间key"}'
```
