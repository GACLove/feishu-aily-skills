# 飞书项目 MCP 完整参考

## 工具清单

### 1. get_workitem_info

获取工作项类型的可用字段与角色信息。

**参数：**
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| work_item_type | string | 是 | 工作项类型名称或系统标识，如 story、需求、issue、缺陷 |
| project_key | string | 否 | 空间 projectKey 或 simpleName |
| url | string | 否 | 飞书项目链接，可自动解析 |

### 2. search_by_mql

使用 MOQL 查询工作项数据。

**参数：**
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| project_key | string | 是 | 空间标识（支持名称、simpleName、projectKey） |
| moql | string | 是 | MOQL 查询语句 |
| session_id | string | 否 | 分页会话 ID |
| group_pagination_list | array | 否 | 分页信息 |

### 3. list_todo

获取当前用户的待办/已办工作项。

**参数：**
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| action | string | 是 | 查询类型：todo(待办)/done(已办)/overdue(逾期)/this_week(本周) |
| page_num | number | 是 | 页码，从 1 开始，每页 50 条 |
| asset_key | string | 否 | 工作区 key，报错需要选择时才传 |

### 4. list_schedule

获取指定人员的排期与工作量明细。

**参数：**
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| project_key | string | 是 | 空间标识 |
| user_keys | array | 是 | 用户标识列表（名称/邮箱/userkey），最多 20 个 |
| start_time | string | 是 | 开始时间，格式：2006-01-01 |
| end_time | string | 是 | 结束时间，格式：2006-01-01（最大范围 3 个月） |
| work_item_type_keys | array | 否 | 工作项类型列表，查询所有传入 `_all` |

### 5. create_workitem

创建工作项实例。

**参数：**
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| work_item_type | string | 是 | 工作项类型 |
| project_key | string | 否 | 空间标识 |
| fields | array | 否 | 字段值列表，每项含 field_key 和 field_value |
| url | string | 否 | 可从链接解析空间信息 |

### 6. update_field

更新工作项字段值。

**参数：**
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| work_item_id | string | 是 | 工作项 ID 或名称 |
| project_key | string | 否 | 空间标识 |
| fields | array | 是 | 要更新的字段列表 |
| url | string | 否 | 可从链接解析信息 |

### 7. get_workitem_brief

获取工作项概况。

**参数：**
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| work_item_id | string | 是 | 工作项 ID 或名称 |
| project_key | string | 否 | 空间标识 |
| fields | array | 否 | 要查询的字段 key 或名称 |
| url | string | 否 | 可从链接解析信息 |

### 8. get_view_detail

获取视图详情。

**参数：**
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| view_id | string | 是 | 视图 ID |
| project_key | string | 否 | 空间标识 |
| page_num | number | 否 | 分页页数起点 |
| fields | array | 否 | 要查询的字段 |
| url | string | 否 | 可从链接解析信息 |

### 9. get_node_detail

获取节点详情。

**参数：**
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| work_item_id | string | 是 | 工作项 ID 或名称 |
| node_id | string | 是 | 节点 ID 或名称 |
| project_key | string | 否 | 空间标识 |
| url | string | 否 | 可从链接解析信息 |

### 10. finish_node

完成节点流转。

**参数：**
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| work_item_id | string | 是 | 工作项 ID 或名称 |
| node_id | string | 是 | 节点 ID 或名称 |
| project_key | string | 否 | 空间标识 |
| url | string | 否 | 可从链接解析信息 |

---

## MOQL 语法详解

### 基础语法

MOQL 基于 MySQL 语法扩展，基本结构：

```sql
SELECT `字段名1`, `字段名2` 
FROM `空间名`.`工作项类型` 
WHERE 条件
```

### 相对时间函数

用于查询相对当前时间的日期范围：

| 函数 | 说明 |
|------|------|
| RELATIVE_DATETIME_EQ(col, 'date_para', 'days') | 等于 |
| RELATIVE_DATETIME_GT(col, 'date_para', 'days') | 大于 |
| RELATIVE_DATETIME_GE(col, 'date_para', 'days') | 大于等于 |
| RELATIVE_DATETIME_LT(col, 'date_para', 'days') | 小于 |
| RELATIVE_DATETIME_LE(col, 'date_para', 'days') | 小于等于 |
| RELATIVE_DATETIME_BETWEEN(col, 'date_para', 'days') | 范围内 |

**date_para 可选值：**
- `today` - 今天
- `yesterday` - 昨天
- `tomorrow` - 明天
- `current_week` - 本周
- `next_week` - 下周
- `last_week` - 上周
- `current_month` - 本月
- `next_month` - 下月
- `last_month` - 上月
- `future` - 未来
- `past` - 过去

**示例：**
```sql
-- 今天创建的工作项
RELATIVE_DATETIME_EQ(`创建时间`, 'today')

-- 3天内到期的工作项
RELATIVE_DATETIME_LE(`截止时间`, 'future', '3d')

-- 上周创建的需求
RELATIVE_DATETIME_BETWEEN(`创建时间`, 'last_week')

-- 本月更新的任务
RELATIVE_DATETIME_BETWEEN(`更新时间`, 'current_month')
```

### 数组操作函数

工作项的多选字段、负责人等通常以数组形式存储：

| 函数 | 说明 |
|------|------|
| array_contains(array_col, element) | 数组是否包含某元素 |
| any_match(array_col, predicate) | 是否有任一元素满足条件 |
| all_match(array_col, predicate) | | 是否所有元素满足条件 |
| none_match(array_col, predicate) | 是否所有元素都不满足条件 |
| array_cardinality(array_col) | 数组元素个数 |
| array_filter(array_col, predicate) | 过滤数组 |

**示例：**
```sql
-- 当前负责人包含张三
array_contains(`当前负责人`, '张三')

-- 当前负责人包含当前登录用户或李四
any_match(`当前负责人`, x -> x in (current_login_user(), '李四'))

-- 所有处理人都在后端团队中
all_match(`处理人`, usr -> usr in team(true, '后端开发团队'))

-- 标签数组为空
array_cardinality(`标签`) = 0
```

### 团队与人员函数

| 函数 | 说明 |
|------|------|
| current_login_user() | 返回当前登录用户的 userkey |
| team(include_manager, '团队名') | 返回团队成员 userkey 数组 |
| participate_roles() | 返回所有参与角色的 rolekey |
| all_participate_persons() | 返回所有参与人的 userkey |

**示例：**
```sql
-- 当前负责人是当前登录用户
array_contains(`当前负责人`, current_login_user())

-- 指派给产品团队（含管理者）
any_match(`当前负责人`, x -> x in team(true, '产品团队'))

-- 指派给研发团队（不含管理者）
any_match(`当前负责人`, x -> x in team(false, '研发团队'))
```

### 角色字段查询

角色字段使用特殊前缀 `__`：

```sql
-- 查询 RD 角色包含张三的需求
SELECT `工作项id` FROM `空间`.`需求` 
WHERE array_contains(__RD, '张三')

-- 查询多个角色条件
SELECT `工作项id` FROM `空间`.`需求` 
WHERE array_contains(__RD, '张三') 
  AND array_contains(__PM, '李四')
```

### 排期字段查询

排期类型的字段使用 `__排期名_开始时间` / `__排期名_结束时间` 格式：

```sql
-- 查询开发周期在某时间段的需求
SELECT `工作项id` FROM `空间`.`需求` 
WHERE `__开发周期_开始时间` > '2025-01-01' 
  AND `__开发周期_结束时间` < '2025-01-31'

-- 查询需求排期跨本月的需求
SELECT `工作项id` FROM `空间`.`需求` 
WHERE `__需求排期_开始时间` <= '2025-03-31' 
  AND `__需求排期_结束时间` >= '2025-03-01'
```

### 复杂查询示例

```sql
-- 本周创建的、指派给产品团队且未完成的 P0 需求
SELECT `工作项id`, `任务名称`, `当前负责人`, `状态`
FROM `产品空间`.`需求`
WHERE RELATIVE_DATETIME_EQ(`创建时间`, 'current_week')
  AND any_match(`当前负责人`, x -> x in team(true, '产品团队'))
  AND `优先级` = 'P0'
  AND `是否冻结` = 0

-- 逾期且未分配的需求
SELECT `工作项id`, `任务名称`, `截止时间`
FROM `产品空间`.`需求`
WHERE RELATIVE_DATETIME_LT(`截止时间`, 'today')
  AND array_cardinality(`当前负责人`) = 0
  AND `是否冻结` = 0

-- 某成员本周待完成的任务（含子任务）
SELECT `工作项id`, `任务名称`, `节点`
FROM `研发空间`.`任务`
WHERE any_match(`当前负责人`, x -> x = '张三')
  AND RELATIVE_DATETIME_BETWEEN(`__排期_开始时间`, 'current_week')
  AND `是否冻结` = 0
```

---

## 字段值格式说明

### 时间字段
- 输入：16 位 Unix 毫秒时间戳（如 `1710734400000`）
- 查询：支持 ISO 日期格式（如 `'2025-03-18'`）或相对时间函数

### 人员字段
- 输入：多个用户用英文逗号分隔（如 `"张三,李四"`）
- 查询：使用 `array_contains` 或 `any_match`

### 布尔字段
- 使用整数：`0` 表示 false，`1` 表示 true
