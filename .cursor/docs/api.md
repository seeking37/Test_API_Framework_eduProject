# 接口文档

域名：

端口：



# 用户管理

### 查询用户列表

#### 基本信息

- 请求方法：POST
- 资源路径：/ssm_web/user/findAllUserByPage
- 接口描述：根据分页查询多个用户组成的列表信息

#### 请求参数

**请求头**

| 参数名        | 参数类型         | 是否必填 | 示例 | 备注     |
| ------------- | ---------------- | -------- | ---- | -------- |
| Authorization | TOKEN            | 是       |      | 用户令牌 |
| Content-Type  | application/json | 是       |      |          |
|               |                  |          |      |          |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名      | 参数类型 | 是否必填 | 示例 | 备注     |
| ----------- | -------- | -------- | ---- | -------- |
| currentPage | int      | 是       |      | 页数     |
| pageSize    | int      | 是       |      | 每页大小 |
|             |          |          |      |          |

```text
POST http://localhost:8090/ssm-web/user/findAllUserByPage HTTP/1.1
Content-Type:application/json
Authorization：5b4a90f4-2188-44af-8475-e114e848d3c7
...

{"currentPage":1,"pageSize":10}
```



#### 返回数据

**响应正文：** 

| 参数名  | 二级参数         | 三级参数                | 参数类型            | 是否必填 | 示例 | 备注             |
| ------- | ---------------- | ----------------------- | ------------------- | -------- | ---- | ---------------- |
| success |                  |                         | boolean             | 是       |      |                  |
| state   |                  |                         | int                 | 是       |      | 结果状态         |
| message |                  |                         |                     | 是       |      | 结果描述         |
| content |                  |                         | JSON Object         | 是       |      |                  |
|         | pageNum          |                         | int                 | 否       |      | 页数             |
|         | pageSize         |                         | int                 | 否       |      | 页大小           |
|         | size             |                         | int                 | 否       |      | 页条数           |
|         | orderBy          |                         | Object              | 否       |      | 排序规则         |
|         | startRow         |                         | int                 | 否       |      | 开始行           |
|         | endRow           |                         | int                 | 否       |      | 结束行           |
|         | total            |                         | int                 | 否       |      | 总数             |
|         | pages            |                         | int                 | 否       |      | 总页数           |
|         | list             |                         | List[ JSON Object ] | 否       |      | 用户列表数据     |
|         |                  | id                      | int                 |          |      | 用户id           |
|         |                  | name                    | string              |          |      | 用户名           |
|         |                  | portrait                | string              |          |      | 用户头像         |
|         |                  | phone                   | string              |          |      | 手机号码         |
|         |                  | password                | string              |          |      | 密码             |
|         |                  | reg_ip                  | string              |          |      | 注册ip           |
|         |                  | account_non_expired     | string              |          |      | 过期时间         |
|         |                  | credentials_non_expired | string              |          |      | 证书过期时间     |
|         |                  | account_non_locked      | string              |          |      | 账户锁           |
|         |                  | status                  | string              |          |      | 冻结状态         |
|         |                  | is_del                  | string              |          |      | 删除标志         |
|         |                  | createTime              | timestamp           |          |      | 创建时间         |
|         |                  | updateTime              | timestamp           |          |      | 修改时间         |
|         | firstPage        |                         |                     |          |      | 第1页编号        |
|         | prePage          |                         |                     |          |      | 上一页编号       |
|         | nextPage         |                         |                     |          |      | 下一页编号       |
|         | lastPage         |                         |                     |          |      | 最后一页编号     |
|         | isFirstPage      |                         |                     |          |      | 是否第一页       |
|         | isLastPage       |                         |                     |          |      | 是否最后一页     |
|         | hasPreviousPage  |                         |                     |          |      | 是否有上一页     |
|         | hasNextPage      |                         |                     |          |      | 是否有下一页     |
|         | navigatePages    |                         |                     |          |      | 导航总数         |
|         | navigatepageNums |                         |                     |          |      | 导航的显示的页数 |
|         |                  |                         |                     |          |      |                  |



报文示例：

```text
{"success":true,"state":200,"message":"响应成功","content":{"pageNum":1,"pageSize":10,"size":10,"orderBy":null,"startRow":1,"endRow":10,"total":12,"pages":2,"list":[{"id":100030011,"name":"15321919666","portrait":"https://edu-lagou.oss-cn-beijing.aliyuncs.com/images/2020/06/28/15933251448762927.png","phone":"15321919666","password":"123456","reg_ip":null,"account_non_expired":null,"credentials_non_expired":null,"account_non_locked":null,"status":"DISABLE","is_del":null,"createTime":1594347555000,"updateTime":null},{"id":100030012,"name":"15588886623","portrait":null,"phone":"15588886623","password":"123456","reg_ip":null,"account_non_expired":null,"credentials_non_expired":null,"account_non_locked":null,"status":"DISABLE","is_del":null,"createTime":1594348981000,"updateTime":null},{"id":100030013,"name":"15588886665","portrait":null,"phone":"15588886665","password":"123456","reg_ip":null,"account_non_expired":null,"credentials_non_expired":null,"account_non_locked":null,"status":"DISABLE","is_del":null,"createTime":1594350551000,"updateTime":null},{"id":100030014,"name":"15588886664","portrait":null,"phone":"15588886664","password":"123456","reg_ip":null,"account_non_expired":null,"credentials_non_expired":null,"account_non_locked":null,"status":"ENABLE","is_del":null,"createTime":1594350626000,"updateTime":null},{"id":100030015,"name":"15588886663","portrait":null,"phone":"15588886663","password":"123456","reg_ip":null,"account_non_expired":null,"credentials_non_expired":null,"account_non_locked":null,"status":"ENABLE","is_del":null,"createTime":1594351310000,"updateTime":null},{"id":100030016,"name":"15588886644","portrait":null,"phone":"15588886644","password":"123456","reg_ip":null,"account_non_expired":null,"credentials_non_expired":null,"account_non_locked":null,"status":"ENABLE","is_del":null,"createTime":1594351436000,"updateTime":null},{"id":100030018,"name":"15588886123","portrait":null,"phone":"15588886123","password":"123456","reg_ip":null,"account_non_expired":null,"credentials_non_expired":null,"account_non_locked":null,"status":"ENABLE","is_del":null,"createTime":1594354655000,"updateTime":null},{"id":100030019,"name":"15588886234","portrait":"https://edu-lagou.oss-cn-beijing.aliyuncs.com/images/2020/07/10/15943594999396473.png","phone":"15588886234","password":"123456","reg_ip":null,"account_non_expired":null,"credentials_non_expired":null,"account_non_locked":null,"status":"ENABLE","is_del":null,"createTime":1594354816000,"updateTime":null},{"id":100030020,"name":"18211111111","portrait":null,"phone":"18211111111","password":"123456","reg_ip":null,"account_non_expired":null,"credentials_non_expired":null,"account_non_locked":null,"status":"ENABLE","is_del":null,"createTime":1594360661000,"updateTime":null},{"id":100030021,"name":"15811112222","portrait":null,"phone":"15811112222","password":"123456","reg_ip":null,"account_non_expired":null,"credentials_non_expired":null,"account_non_locked":null,"status":"ENABLE","is_del":null,"createTime":1594611320000,"updateTime":null}],"firstPage":1,"prePage":0,"nextPage":2,"lastPage":2,"isFirstPage":true,"isLastPage":false,"hasPreviousPage":false,"hasNextPage":true,"navigatePages":8,"navigatepageNums":[1,2]}}
```

自定义状态码描述：

| 参数   | 参数值 | 功能描述                 |
| ------ | ------ | ------------------------ |
| status |        | DISABLE 冻结 ENABLE 启用 |
|        |        |                          |



### 搜索用户

#### 基本信息

- 请求方法：POST
- 资源路径：/ssm_web/user/findAllUserByPage
- 接口描述：根据输入的手机号码和时间范围搜索用户列表

#### 请求参数

**请求头**

| 参数名        | 参数类型         | 是否必填 | 示例 | 备注     |
| ------------- | ---------------- | -------- | ---- | -------- |
| Authorization | TOKEN            | 是       |      | 用户令牌 |
| Content-Type  | application/json | 是       |      |          |
|               |                  |          |      |          |



**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名          | 参数类型 | 是否必填 | 示例        | 备注 |
| --------------- | -------- | -------- | ----------- | ---- |
| currentPage     | int      | 是       |             |      |
| pageSize        | int      | 是       |             |      |
| username        | string   | 否       | 15321919666 |      |
| startCreateTime | string   | 否       | 2025-06-02  |      |
| endCreateTime   | string   | 否       | 2025-06-13  |      |
|                 |          |          |             |      |

#### 返回数据

**响应正文：** 

 

| 参数名  | 二级参数         | 三级参数                | 参数类型            | 是否必填 | 示例 | 备注             |
| ------- | ---------------- | ----------------------- | ------------------- | -------- | ---- | ---------------- |
| success |                  |                         | boolean             | 是       |      |                  |
| state   |                  |                         | int                 | 是       |      | 结果状态         |
| message |                  |                         |                     | 是       |      | 结果描述         |
| content |                  |                         | JSON Object         | 是       |      |                  |
|         | pageNum          |                         | int                 | 否       |      | 页数             |
|         | pageSize         |                         | int                 | 否       |      | 页大小           |
|         | size             |                         | int                 | 否       |      | 页条数           |
|         | orderBy          |                         | Object              | 否       |      | 排序规则         |
|         | startRow         |                         | int                 | 否       |      | 开始行           |
|         | endRow           |                         | int                 | 否       |      | 结束行           |
|         | total            |                         | int                 | 否       |      | 总数             |
|         | pages            |                         | int                 | 否       |      | 总页数           |
|         | list             |                         | List[ JSON Object ] | 否       |      | 用户列表数据     |
|         |                  | id                      | int                 |          |      | 用户id           |
|         |                  | name                    | string              |          |      | 用户名           |
|         |                  | portrait                | string              |          |      | 用户头像         |
|         |                  | phone                   | string              |          |      | 手机号码         |
|         |                  | password                | string              |          |      | 密码             |
|         |                  | reg_ip                  | string              |          |      | 注册ip           |
|         |                  | account_non_expired     | string              |          |      | 过期时间         |
|         |                  | credentials_non_expired | string              |          |      | 证书过期时间     |
|         |                  | account_non_locked      | string              |          |      | 账户锁           |
|         |                  | status                  | string              |          |      | 冻结状态         |
|         |                  | is_del                  | string              |          |      | 删除标志         |
|         |                  | createTime              | timestamp           |          |      | 创建时间         |
|         |                  | updateTime              | timestamp           |          |      | 修改时间         |
|         | firstPage        |                         |                     |          |      | 第1页编号        |
|         | prePage          |                         |                     |          |      | 上一页编号       |
|         | nextPage         |                         |                     |          |      | 下一页编号       |
|         | lastPage         |                         |                     |          |      | 最后一页编号     |
|         | isFirstPage      |                         |                     |          |      | 是否第一页       |
|         | isLastPage       |                         |                     |          |      | 是否最后一页     |
|         | hasPreviousPage  |                         |                     |          |      | 是否有上一页     |
|         | hasNextPage      |                         |                     |          |      | 是否有下一页     |
|         | navigatePages    |                         |                     |          |      | 导航总数         |
|         | navigatepageNums |                         |                     |          |      | 导航的显示的页数 |
|         |                  |                         |                     |          |      |                  |



报文示例：

```text
{"success":true,"state":200,"message":"响应成功","content":{"pageNum":1,"pageSize":10,"size":1,"orderBy":null,"startRow":1,"endRow":1,"total":1,"pages":1,"list":[{"id":100030011,"name":"15321919666","portrait":"https://edu-lagou.oss-cn-beijing.aliyuncs.com/images/2020/06/28/15933251448762927.png","phone":"15321919666","password":"123456","reg_ip":null,"account_non_expired":null,"credentials_non_expired":null,"account_non_locked":null,"status":"DISABLE","is_del":null,"createTime":1594347555000,"updateTime":null}],"firstPage":1,"prePage":0,"nextPage":0,"lastPage":1,"isFirstPage":true,"isLastPage":true,"hasPreviousPage":false,"hasNextPage":false,"navigatePages":8,"navigatepageNums":[1]}}
```

自定义状态码描述：

| 参数   | 参数值 | 功能描述                 |
| ------ | ------ | ------------------------ |
| status |        | DISABLE 冻结 ENABLE 启用 |
|        |        |                          |





### 查询用户权限

#### 基本信息

- 请求方法：GET
- 资源路径：/ssm_web/user/getUserPermissions
- 接口描述：

#### 请求参数

**请求头**

| 参数名        | 参数类型 | 是否必填 | 示例 | 备注 |
| ------------- | -------- | -------- | ---- | ---- |
| Authorization | Token    | 是       |      |      |
| Cookie        |          |          |      |      |
|               |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名  | 二级参数     | 三级参数    | 参数类型    | 是否必填 | 示例 | 备注 |
| ------- | ------------ | ----------- | ----------- | -------- | ---- | ---- |
| success |              |             | boolean     | 是       |      |      |
| state   |              |             | int         | 是       |      |      |
| message |              |             | string      | 是       |      |      |
| content |              |             | Json Object | 是       |      |      |
|         | menuList     |             | Json Object | 是       |      |      |
|         |              | subMenuList | Json Object | 否       |      |      |
|         |              | id          | int         | 否       |      |      |
|         |              | parentId    | string      | 否       |      |      |
|         |              | href        | string      | 否       |      |      |
|         |              | icon        | string      | 否       |      |      |
|         |              | name        | string      | 否       |      |      |
|         |              | description | string      | 否       |      |      |
|         |              | orderNum    | string      | 否       |      |      |
|         |              | shown       | string      | 否       |      |      |
|         |              | level       | string      | 否       |      |      |
|         |              | createdTime | string      | 否       |      |      |
|         |              | updatedTime | string      | 否       |      |      |
|         | resourceList |             | Json Object | 是       |      |      |
|         |              | id          | string      | 否       |      |      |
|         |              | name        | string      | 否       |      |      |
|         |              | url         | string      | 否       |      |      |
|         |              | categoryId  | string      | 否       |      |      |
|         |              | description | string      | 否       |      |      |
|         |              | createdTime | string      | 否       |      |      |
|         |              | updatedTime | string      | 否       |      |      |
|         |              | createdBy   | string      | 否       |      |      |
|         |              | updatedBy   | string      | 否       |      |      |
|         |              | subMenuList | Json Object | 否       |      |      |
|         |              |             |             |          |      |      |



报文示例：

```text
{
	"success": true,
	"state": 200,
	"message": "响应成功",
	"content": {
		"menuList": [{
			"id": 1,
			"parentId": -1,
			"href": "",
			"icon": "lock",
			"name": "权限管理",
			"description": null,
			"orderNum": 1,
			"shown": 1,
			"level": 0,
			"createdTime": null,
			"updatedTime": null,
			"createdBy": null,
			"updatedBy": null,
			"subMenuList": [{
				"id": 22,
				"parentId": 1,
				"href": "addOrder",
				"icon": "lock",
				"name": "订单管理修改",
				"description": "订单系统管理修改",
				"orderNum": 1,
				"shown": 0,
				"level": 0,
				"createdTime": 1597062761000,
				"updatedTime": 1597062761000,
				"createdBy": "system",
				"updatedBy": "system",
				"subMenuList": []
			}]
		}],
		"resourceList": [{
			"id": 1,
			"name": "获取所有角色001",
			"url": "/boss/role/all",
			"categoryId": 1,
			"description": "获取所有角色",
			"createdTime": null,
			"updatedTime": null,
			"createdBy": null,
			"updatedBy": null
		}]
	}
}
```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 登陆

#### 基本信息

- 请求方法：POST
- 资源路径：/ssm_web/user/login
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名   | 参数类型 | 是否必填 | 示例 | 备注 |
| -------- | -------- | -------- | ---- | ---- |
| phone    | string   | 是       |      |      |
| password | string   | 是       |      |      |
|          |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名  | 二级参数     | 三级参数                | 参数类型    | 是否必填 | 示例 | 备注 |
| ------- | ------------ | ----------------------- | ----------- | -------- | ---- | ---- |
| success |              |                         | string      | 是       |      |      |
| state   |              |                         | string      | 是       |      |      |
| message |              |                         | string      | 是       |      |      |
| content |              |                         | JSON Object | 是       |      |      |
|         | access_token |                         | string      | 否       |      |      |
|         | user_id      |                         | string      | 否       |      |      |
|         | user         |                         | JSON Object | 否       |      |      |
|         |              | id                      | string      | 否       |      |      |
|         |              | name                    | string      | 否       |      |      |
|         |              | portrait                | string      | 否       |      |      |
|         |              | phone                   | string      | 否       |      |      |
|         |              | password                | string      | 否       |      |      |
|         |              | reg_ip                  | string      | 否       |      |      |
|         |              | account_non_expired     | string      | 否       |      |      |
|         |              | credentials_non_expired | string      | 否       |      |      |
|         |              | account_non_locked      | string      | 否       |      |      |
|         |              | status                  | string      | 否       |      |      |
|         |              | is_del                  | string      | 否       |      |      |
|         |              | createTime              | timestamp   | 否       |      |      |
|         |              | updateTime              | timestamp   | 否       |      |      |

报文示例：

```text
{
 "success": true,
 "state": 1,
 "message": "响应成功",
 "content": {
  "access_token": "e26d5ba4-24a4-455c-b683-8a11bc78053c",
  "user_id": 100030011,
  "user": {
   "id": 100030011,
   "name": "15321919666",
   "portrait": "https://edu-lagou.oss-cn-beijing.aliyuncs.com/images/2020/06/28/15933251448762927.png",
   "phone": "15321919666",
   "password": "123456",
   "reg_ip": null,
   "account_non_expired": null,
   "credentials_non_expired": null,
   "account_non_locked": null,
   "status": "DISABLE",
   "is_del": null,
   "createTime": 1594347555000,
   "updateTime": 1594347555000
  }
 }
}
```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 冻结/解冻用户

#### 基本信息

- 请求方法：POST
- 资源路径：/ssm_web/user/updateUserStatus?id=100030011&status=DISABLE
- 接口描述：

#### 请求参数

**请求头**

| 参数名            | 参数类型 | 是否必填 | 示例 | 备注 |
| ----------------- | -------- | -------- | ---- | ---- |
| **Authorization** | Token    | 是       |      |      |
| **Cookie**        |          | 是       |      |      |
|                   |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例           | 备注 |
| ------ | -------- | -------- | -------------- | ---- |
| id     |          |          |                |      |
| status |          |          | DISABLE/ENABLE |      |
|        |          |          |                |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text
{"success":true,"state":200,"message":"响应成功","content":"DISABLE"}
```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 修改用户角色权限

#### 基本信息

- 请求方法：POST
- 资源路径：/ssm_web/user/userContextRole
- 接口描述：

#### 请求参数

**请求头**

| 参数名        | 参数类型         | 是否必填 | 示例 | 备注 |
| ------------- | ---------------- | -------- | ---- | ---- |
| Content-Type  | application/json | 是       |      |      |
| Authorization |                  | 是       |      |      |
| Cookie        |                  | 是       |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

{"userId":100030011,"roleIdList":[2,7,4]}

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



# 课程管理



### 查询所有课程

#### 基本信息

- 请求方法：POST
- 资源路径：/ssm_web/course/findAllCourse
- 接口描述：

#### 请求参数

**请求头**

| 参数名        | 参数类型                                          | 是否必填 | 示例 | 备注 |
| ------------- | ------------------------------------------------- | -------- | ---- | ---- |
| Content-Type  | application/json                                  | 是       |      |      |
| Cookie        | {"JSESSIONID":"24433E9DA6E8F364DDC13D864383580B"} | 是       |      |      |
| Authorization | Token                                             | 是       |      |      |



**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名  | 二级参数                  | 参数类型      | 是否必填 | s示例 | 备注 |
| ------- | ------------------------- | ------------- | -------- | ----- | ---- |
| success |                           | boolean       | 是       |       |      |
| state   |                           | int           | 是       |       |      |
| message |                           | string        | 是       |       |      |
| content |                           | List Object[] | 是       |       |      |
|         | id                        | int           | 否       |       |      |
|         | courseName                | string        | 否       |       |      |
|         | brief                     | string        | 否       |       |      |
|         | price                     | string        | 否       |       |      |
|         | priceTag                  | string        | 否       |       |      |
|         | discounts                 | string        | 否       |       |      |
|         | discountsTag              | string        | 否       |       |      |
|         | courseDescriptionMarkDown | string        | 否       |       |      |
|         | courseDescription         | string        | 否       |       |      |
|         | courseImgUrl              | string        | 否       |       |      |
|         | isNew                     | string        | 否       |       |      |
|         | isNewDes                  | string        | 否       |       |      |
|         | lastOperatorId            | string        | 否       |       |      |
|         | autoOnlineTime            | string        | 否       |       |      |
|         | createTime                | timestamp     | 否       |       |      |
|         | updateTime                | timestamp     | 否       |       |      |
|         | isDel                     | string        | 否       |       |      |
|         | totalDuration             | string        | 否       |       |      |
|         | courseListImg             | string        | 否       |       |      |
|         | status                    | string        | 否       |       |      |
|         | sortNum                   | string        | 否       |       |      |
|         | previewFirstField         | string        | 否       |       |      |
|         | previewSecondField        | string        | 否       |       |      |
|         | sales                     | string        | 否       |       |      |

报文示例：

```text
{"success":true,"state":200,"message":"响应成功","content":[{"id":40,"courseName":"测试修改课程","brief":null,"price":1.0,"priceTag":null,"discounts":0.0,"discountsTag":null,"courseDescriptionMarkDown":null,"courseDescription":null,"courseImgUrl":null,"isNew":0,"isNewDes":null,"lastOperatorId":0,"autoOnlineTime":null,"createTime":null,"updateTime":null,"isDel":0,"totalDuration":0,"courseListImg":null,"status":0,"sortNum":0,"previewFirstField":null,"previewSecondField":null,"sales":0}}]}
```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 根据课程ID查询课程

#### 基本信息

- 请求方法：GET

- 资源路径：/ssm_web/courseContent/findCourseByCourseId

- 接口描述：

#### 请求参数

**请求头**

| 参数名        | 参数类型                                          | 是否必填 | 示例 | 备注 |
| ------------- | ------------------------------------------------- | -------- | ---- | ---- |
|               |                                                   | 是       |      |      |
| Cookie        | {"JSESSIONID":"24433E9DA6E8F364DDC13D864383580B"} | 是       |      |      |
| Authorization | Token                                             | 是       |      |      |



**查询参数** 

| 参数名   | 参数类型 | 是否必填 | 示例 | 备注 |
| -------- | -------- | -------- | ---- | ---- |
| courseId | int      |          |      |      |
|          |          |          |      |      |
|          |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名  | 二级参数                  | 参数类型    | 是否必填 | s示例 | 备注 |
| ------- | ------------------------- | ----------- | -------- | ----- | ---- |
| success |                           | boolean     | 是       |       |      |
| state   |                           | int         | 是       |       |      |
| message |                           | string      | 是       |       |      |
| content |                           | JSON Object | 是       |       |      |
|         | id                        | int         | 否       |       |      |
|         | courseName                | string      | 否       |       |      |
|         | brief                     | string      | 否       |       |      |
|         | price                     | string      | 否       |       |      |
|         | priceTag                  | string      | 否       |       |      |
|         | discounts                 | string      | 否       |       |      |
|         | discountsTag              | string      | 否       |       |      |
|         | courseDescriptionMarkDown | string      | 否       |       |      |
|         | courseDescription         | string      | 否       |       |      |
|         | courseImgUrl              | string      | 否       |       |      |
|         | isNew                     | string      | 否       |       |      |
|         | isNewDes                  | string      | 否       |       |      |
|         | lastOperatorId            | string      | 否       |       |      |
|         | autoOnlineTime            | string      | 否       |       |      |
|         | createTime                | timestamp   | 否       |       |      |
|         | updateTime                | timestamp   | 否       |       |      |
|         | isDel                     | string      | 否       |       |      |
|         | totalDuration             | string      | 否       |       |      |
|         | courseListImg             | string      | 否       |       |      |
|         | status                    | string      | 否       |       |      |
|         | sortNum                   | string      | 否       |       |      |
|         | previewFirstField         | string      | 否       |       |      |
|         | previewSecondField        | string      | 否       |       |      |
|         | sales                     | string      | 否       |       |      |

报文示例：

```text
{"success":true,"state":200,"message":"响应成功","content":{"id":220,"courseName":"测试开发","brief":null,"price":0.0,"priceTag":null,"discounts":0.0,"discountsTag":null,"courseDescriptionMarkDown":null,"courseDescription":null,"courseImgUrl":null,"isNew":0,"isNewDes":null,"lastOperatorId":0,"autoOnlineTime":null,"createTime":null,"updateTime":null,"isDel":0,"totalDuration":0,"courseListImg":null,"status":0,"sortNum":0,"previewFirstField":null,"previewSecondField":null,"sales":0}}

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 新增课程

#### 基本信息

- 请求方法：POST
- 资源路径：/ssm_web/course/saveOrUpdateCourse
- 接口描述：

#### 请求参数

**请求头**



| 参数名        | 参数类型                                          | 是否必填 | 示例 | 备注 |
| ------------- | ------------------------------------------------- | -------- | ---- | ---- |
| Content-Type  | application/json                                  | 是       |      |      |
| Cookie        | {"JSESSIONID":"24433E9DA6E8F364DDC13D864383580B"} | 是       |      |      |
| Authorization | Token                                             | 是       |      |      |



**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名                    | 二级参数 | 参数类型    | 是否必填 | 示例 | 备注 |
| ------------------------- | -------- | ----------- | -------- | ---- | ---- |
| brief                     |          | string      | 是       |      | 简介 |
| courseDescriptionMarkDown |          | string      | 否       |      |      |
| courseImgUrl              |          | string      | 否       |      |      |
| courseListImg             |          | string      | 否       |      |      |
| courseName                |          | string      | 是       |      |      |
| discounts                 |          | string      | 否       |      |      |
| discountsTag              |          | string      | 否       |      |      |
| id                        |          | string      | 否       |      |      |
| previewFirstField         |          | string      | 是       |      |      |
| previewSecondField        |          | string      | 否       |      |      |
| price                     |          | string      | 否       |      |      |
| sales                     |          | string      | 否       |      |      |
| sortNum                   |          | string      | 否       |      |      |
| status                    |          | string      | 否       |      |      |
| teacherName               |          | string      | 否       |      |      |
| position                  |          | string      | 否       |      |      |
| description               |          | string      | 否       |      |      |
| teacherDTO                |          | Json Object | 否       |      |      |
| activityCourse            |          | string      | 否       |      |      |
| activityCourseDTO         |          | Json Object | 否       |      |      |

```text
{"brief":"简介","courseDescriptionMarkDown":"","courseImgUrl":"","courseListImg":"","courseName":"测试添加课程","discounts":"1","discountsTag":"泰坦","id":"","previewFirstField":"这是一个测试用视频","previewSecondField":"这是一个测试用视频","price":"1","sales":"1","sortNum":"","status":"","teacherName":"泰坦","position":"讲师","description":"讲师简介","teacherDTO":{},"activityCourse":false,"activityCourseDTO":{}}

```



#### 返回数据

**响应正文：** 

| 参数名  | 参数类型    | 是否必填 | 示例 | 备注 |
| ------- | ----------- | -------- | ---- | ---- |
| success | boolean     | 是       |      |      |
| state   | int         | 是       |      |      |
| message | string      | 是       |      |      |
| content | JSON Object | 是       |      |      |

报文示例：

```text
{
 "success": true,
 "state": 200,
 "message": "响应成功",
 "content": null
}

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 修改课程

#### 基本信息

- 请求方法：POST
- 资源路径：/ssm_web/course/saveOrUpdateCourse
- 接口描述：

#### 请求参数

**请求头**



| 参数名        | 参数类型                                          | 是否必填 | 示例 | 备注 |
| ------------- | ------------------------------------------------- | -------- | ---- | ---- |
| Content-Type  | application/json                                  | 是       |      |      |
| Cookie        | {"JSESSIONID":"24433E9DA6E8F364DDC13D864383580B"} | 是       |      |      |
| Authorization | Token                                             | 是       |      |      |



**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名                    | 二级参数 | 参数类型    | 是否必填 | 示例 | 备注 |
| ------------------------- | -------- | ----------- | -------- | ---- | ---- |
| brief                     |          | string      | 是       |      |      |
| courseDescriptionMarkDown |          | string      | 否       |      |      |
| courseImgUrl              |          | string      | 否       |      |      |
| courseListImg             |          | string      | 否       |      |      |
| courseName                |          | string      | 是       |      |      |
| discounts                 |          | string      | 否       |      |      |
| discountsTag              |          | string      | 否       |      |      |
| id                        |          | string      | 否       |      |      |
| previewFirstField         |          | string      | 是       |      |      |
| previewSecondField        |          | string      | 否       |      |      |
| price                     |          | string      | 否       |      |      |
| sales                     |          | string      | 否       |      |      |
| sortNum                   |          | string      | 否       |      |      |
| status                    |          | string      | 否       |      |      |
| teacherName               |          | string      | 否       |      |      |
| position                  |          | string      | 否       |      |      |
| description               |          | string      | 否       |      |      |
| teacherDTO                |          | Json Object | 否       |      |      |
| activityCourse            |          | string      | 否       |      |      |
| activityCourseDTO         |          | Json Object | 否       |      |      |

```text
{"brief":"简介","courseDescriptionMarkDown":"","courseImgUrl":"","courseListImg":"","courseName":"测试添加课程","discounts":"1","discountsTag":"泰坦","id":"","previewFirstField":"这是一个测试用视频","previewSecondField":"这是一个测试用视频","price":"1","sales":"1","sortNum":"","status":"","teacherName":"泰坦","position":"讲师","description":"讲师简介","teacherDTO":{},"activityCourse":false,"activityCourseDTO":{}}

```



#### 返回数据

**响应正文：** 

| 参数名  | 参数类型    | 是否必填 | 示例 | 备注 |
| ------- | ----------- | -------- | ---- | ---- |
| success | boolean     | 是       |      |      |
| state   | int         | 是       |      |      |
| message | string      | 是       |      |      |
| content | JSON Object | 是       |      |      |

报文示例：

```text
{
 "success": true,
 "state": 200,
 "message": "响应成功",
 "content": null
}

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 更新课程状态

#### 基本信息

- 请求方法：GET
- 资源路径：/ssm_web/course/updateCourseStatus
- 接口描述：

#### 请求参数

**请求头**



| 参数名        | 参数类型                                          | 是否必填 | 示例 | 备注 |
| ------------- | ------------------------------------------------- | -------- | ---- | ---- |
| Content-Type  | application/json                                  | 是       |      |      |
| Cookie        | {"JSESSIONID":"24433E9DA6E8F364DDC13D864383580B"} | 是       |      |      |
| Authorization | Token                                             | 是       |      |      |



**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
| status | int      | 是       | 1    |      |
| id     | int      | 是       | 35   |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名  | 二级参数 | 参数类型    | 是否必填 | 示例 | 备注 |
| ------- | -------- | ----------- | -------- | ---- | ---- |
| success |          | boolean     | 是       |      |      |
| state   |          | int         | 是       |      |      |
| message |          | string      | 是       |      |      |
| content |          | JSON Object | 是       |      |      |
|         | status   | int         | 是       |      |      |

报文示例：

```text
{"success":true,"state":200,"message":"响应成功","content":{"status":1}}

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 查询课程章节

#### 基本信息

- 请求方法：GET
- 资源路径：/ssm_web/courseContent/findSectionAndLesson
- 接口描述：

#### 请求参数

**请求头**

| 参数名        | 参数类型 | 是否必填 | 示例 | 备注 |
| ------------- | -------- | -------- | ---- | ---- |
| Authorization | Token    |          |      |      |
| Cookie        |          |          |      |      |
|               |          |          |      |      |

**查询参数** 

| 参数名   | 参数类型 | 是否必填 | 示例 | 备注 |
| -------- | -------- | -------- | ---- | ---- |
| courseId | int      | s否      |      |      |
|          |          |          |      |      |
|          |          |          |      |      |

**请求体** 

请求体示例：

```text
{"courseId":220,"courseName":"测试开发","sectionName":"接口测试基础理论","description":"夯实基础","orderNum":"1"}

```



#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text
{"success":true,"state":200,"message":"响应成功","content":[{"id":24,"courseId":220,"sectionName":"接口测试基础理论","description":"夯实基础","createTime":null,"updateTime":null,"isDe":0,"orderNum":1,"status":0,"lessonList":[{"id":null,"courseId":220,"sectionId":0,"theme":null,"duration":0,"isFree":0,"createTime":null,"updateTime":null,"isDel":0,"orderNum":1,"status":0}]}]}

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 新增课程章节

#### 基本信息

- 请求方法：POST
- 资源路径：/ssm_web/courseContent/saveOrUpdateSection
- 接口描述：

#### 请求参数

**请求头**

| 参数名        | 参数类型 | 是否必填 | 示例 | 备注 |
| ------------- | -------- | -------- | ---- | ---- |
| Authorization |          |          |      |      |
| Cookie        |          |          |      |      |
|               |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名      | 参数类型 | 是否必填 | 示例 | 备注 |
| ----------- | -------- | -------- | ---- | ---- |
| courseId    | int      | 是       |      |      |
| courseName  | string   | 是       |      |      |
| sectionName | string   | 是       |      |      |
| description | string   | 否       |      |      |
| orderNum    | string   | 否       |      |      |
|             |          |          |      |      |

请求体示例：

```text
{"courseId":220,"courseName":"测试开发","sectionName":"接口测试基础理论","description":"夯实基础","orderNum":"1"}


```



#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text
{"success":true,"state":200,"message":"响应成功","content":null}


```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |





### 修改课程章节

#### 基本信息

- 请求方法：POST
- 资源路径：/ssm_web/courseContent/saveOrUpdateSection
- 接口描述：

#### 请求参数

**请求头**

| 参数名        | 参数类型 | 是否必填 | 示例 | 备注 |
| ------------- | -------- | -------- | ---- | ---- |
| Authorization |          |          |      |      |
| Cookie        |          |          |      |      |
|               |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名      | 参数类型 | 是否必填 | 示例 | 备注 |
| ----------- | -------- | -------- | ---- | ---- |
| courseId    | int      | 是       |      |      |
| courseName  | string   | 是       |      |      |
| sectionName | string   | 是       |      |      |
| description | string   | 否       |      |      |
| orderNum    | string   | 否       |      |      |
|             |          |          |      |      |

请求体示例：

```text
{"courseId":220,"courseName":"测试开发","sectionName":"接口测试基础理论","description":"夯实基础","orderNum":"1"}


```



#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text
{"success":true,"state":200,"message":"响应成功","content":null}


```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 更新课程章节状态

#### 基本信息

- 请求方法：GET
- 资源路径：/ssm_web/courseContent/updateSectionStatus
- 接口描述：

#### 请求参数

**请求头**

| 参数名        | 参数类型 | 是否必填 | 示例 | 备注 |
| ------------- | -------- | -------- | ---- | ---- |
| Authorization |          |          |      |      |
| Cookie        |          |          |      |      |
|               |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
| id     | int      | 是       |      |      |
| status | int      | 是       |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text
{"success":true,"state":200,"message":"响应成功","content":{"status":2}}


```

自定义状态码描述：

| 参数   | 参数值 | 功能描述                             |
| ------ | ------ | ------------------------------------ |
| status |        | 0:已隐藏<br />1:待更新<br />2:已更新 |
|        |        |                                      |



# 权限管理



## 角色列表

### 查询角色

#### 基本信息

- 请求方法：/ssm_web/
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 添加角色

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 修改角色

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 删除角色

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 根据角色搜索菜单权限

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 分配菜单

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 根据角色搜索资源权限

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 分配资源

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |





## 菜单列表

### 查询菜单列表

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 搜索菜单

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 新增菜单

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 修改菜单

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 删除菜单

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |







## 资源列表



### 查询资源列表

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 搜索资源

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 添加资源

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 修改资源

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 删除资源

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 查询资源分类列表

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 添加资源分类

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 修改资源分类

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |



### 删除资源分类

#### 基本信息

- 请求方法：
- 资源路径：
- 接口描述：

#### 请求参数

**请求头**

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**查询参数** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

**请求体** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

#### 返回数据

**响应正文：** 

| 参数名 | 参数类型 | 是否必填 | 示例 | 备注 |
| ------ | -------- | -------- | ---- | ---- |
|        |          |          |      |      |
|        |          |          |      |      |
|        |          |          |      |      |

报文示例：

```text

```

自定义状态码描述：

| 参数 | 参数值 | 功能描述 |
| ---- | ------ | -------- |
|      |        |          |
|      |        |          |

