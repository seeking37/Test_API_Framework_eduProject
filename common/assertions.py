import traceback
import allure
import jsonpath
import operator

from pymysql import DatabaseError

from common.recordlog import logs
from common.connection import ConnectMysql


class Assertions:
    """"
    接口断言模式，支持
    1）响应文本字符串包含模式断言
    2）响应结果相等断言
    3）响应结果不相等断言
    4）响应结果任意值断言
    5）数据库相等断言

    """

    def contains_assert(self, value, response, status_code):
        """
        字符串包含断言模式，断言预期结果的字符串是否包含在接口的响应信息中
        :param value: 预期结果，yaml文件的预期结果值
        :param response: 接口实际响应结果
        :param status_code: 响应状态码
        :return: 返回结果的状态标识
        """
        # 断言状态标识，0成功，其他失败
        flag = 0
        for assert_key, assert_value in value.items():
            # 单独判断status_code字段
            if assert_key == "status_code":
                flag += self.status_code_eq_assert(assert_value, status_code)
            else:
                resp_list = jsonpath.jsonpath(response, "$..%s" % assert_key)
                # 情况1：完全未找到路径（返回False）
                if resp_list is False:
                    flag += 1
                    allure.attach(f"Key '{assert_key}' not found in response",
                                  "JSONPath匹配失败",
                                  attachment_type=allure.attachment_type.TEXT)
                    logs.error(f"响应键缺失断言失败：未找到【{assert_key}】")
                    continue  # 跳过后续步骤
                # 情况2：路径存在但值为空容器（如 []）
                if not resp_list:  # 空列表 [] 也视为失败
                    flag += 1
                    allure.attach(f"Key '{assert_key}' exists but is empty (e.g. [])",
                                  "空值断言失败",
                                  attachment_type=allure.attachment_type.TEXT)
                    logs.error(f"响应键值空断言失败：【{assert_key}】值为空")
                    continue
                if isinstance(resp_list[0], str):
                    resp_list = ''.join(resp_list)
                if resp_list:
                    assert_value = None if str(assert_value).upper() == 'NONE' else assert_value
                    if assert_value in resp_list:
                        allure.attach(f"{assert_key}预期结果：{assert_value}\n实际结果：{resp_list}",
                                      '响应文本断言结果：成功',
                                      attachment_type=allure.attachment_type.TEXT)
                        logs.info(
                            "响应文本断言成功：【%s】预期结果【%s】,实际结果【%s】" % (assert_key, assert_value, resp_list))
                    else:
                        flag = flag + 1
                        allure.attach(f"{assert_key}预期结果：{assert_value}\n实际结果：{resp_list}",
                                      '响应文本断言结果：失败',
                                      attachment_type=allure.attachment_type.TEXT)
                        logs.error("响应文本断言失败：【%s】预期结果为【%s】,实际结果为【%s】" % (
                        assert_key, assert_value, resp_list))
        return flag

    def equal_assert(self, expected_results, actual_results, status_code):
        flag = 0

        # 处理 status_code
        for json_path, expected_value in expected_results.items():
            if json_path == "status_code":
                flag += self.status_code_eq_assert(expected_value, status_code)
            else:
                # 使用 JSONPath 查找
                result = jsonpath.jsonpath(actual_results, json_path)

                # 处理未找到的情况
                if result is False:
                    flag += 1
                    logs.error(f"相等断言失败：JSONPath '{json_path}' 未匹配到结果")
                    allure.attach(f"JSONPath '{json_path}' 未匹配到结果",
                                  "相等断言失败",
                                  attachment_type=allure.attachment_type.TEXT)
                    continue

                # 处理匹配到多个值的情况
                if len(result) > 1:
                    flag += 1
                    logs.error(f"相等断言失败：JSONPath '{json_path}' 匹配到多个值 ({len(result)} 个)")
                    allure.attach(f"JSONPath '{json_path}' 匹配到多个值 ({len(result)} 个)\n匹配结果: {result}",
                                  "相等断言失败",
                                  attachment_type=allure.attachment_type.TEXT)
                    continue

                # 获取实际值
                actual_value = result[0]

                # 比较值
                if actual_value == expected_value:
                    logs.info(f"相等断言成功：JSONPath '{json_path}' 预期值: {expected_value}, 实际值: {actual_value}")
                    allure.attach(f"JSONPath '{json_path}':\n预期值: {expected_value}\n实际值: {actual_value}",
                                  "相等断言结果：成功",
                                  attachment_type=allure.attachment_type.TEXT)
                else:
                    flag += 1
                    logs.error(f"相等断言失败：JSONPath '{json_path}' 预期值: {expected_value}, 实际值: {actual_value}")
                    allure.attach(f"JSONPath '{json_path}':\n预期值: {expected_value}\n实际值: {actual_value}",
                                  "相等断言结果：失败",
                                  attachment_type=allure.attachment_type.TEXT)

        return flag

    def not_equal_assert(self, expected_results, actual_results, status_code):
        flag = 0

        # 处理 status_code
        for json_path, expected_value in expected_results.items():
            if json_path == "status_code":
                # 使用不相等断言检查状态码
                flag += self.status_code_neq_assert(expected_value, status_code)
            else:
                # 使用 JSONPath 查找
                result = jsonpath.jsonpath(actual_results, json_path)

                # 处理未找到的情况
                if result is False:
                    # 路径不存在视为成功（因为实际不存在 ≠ 预期值）
                    logs.info(f"不相等断言成功：JSONPath '{json_path}' 未匹配到结果（实际不存在）")
                    allure.attach(f"JSONPath '{json_path}' 未匹配到结果（实际不存在）",
                                  "不相等断言成功",
                                  attachment_type=allure.attachment_type.TEXT)
                    continue

                # 处理匹配到多个值的情况
                if len(result) > 1:
                    flag += 1
                    logs.error(f"不相等断言失败：JSONPath '{json_path}' 匹配到多个值 ({len(result)} 个)")
                    allure.attach(f"JSONPath '{json_path}' 匹配到多个值 ({len(result)} 个)\n匹配结果: {result}",
                                  "不相等断言失败",
                                  attachment_type=allure.attachment_type.TEXT)
                    continue

                # 获取实际值
                actual_value = result[0]

                # 比较值：当实际值 ≠ 预期值时成功
                if actual_value != expected_value:
                    logs.info(f"不相等断言成功：JSONPath '{json_path}' 预期值: {expected_value}, 实际值: {actual_value}")
                    allure.attach(f"JSONPath '{json_path}':\n预期值: {expected_value}\n实际值: {actual_value}",
                                  "不相等断言结果：成功",
                                  attachment_type=allure.attachment_type.TEXT)
                else:
                    flag += 1
                    logs.error(f"不相等断言失败：JSONPath '{json_path}' 实际值等于预期值: {expected_value}")
                    allure.attach(f"JSONPath '{json_path}':\n预期值: {expected_value}\n实际值: {actual_value}",
                                  "不相等断言结果：失败",
                                  attachment_type=allure.attachment_type.TEXT)

        return flag

    def assert_response_time(self, res_time, exp_time):
        """
        通过断言接口的响应时间与期望时间对比,接口响应时间小于预期时间则为通过
        :param res_time: 接口的响应时间
        :param exp_time: 预期的响应时间
        :return:
        """
        try:
            assert res_time < exp_time
            return True
        except Exception as e:
            logs.error('接口响应时间[%ss]大于预期时间[%ss]' % (res_time, exp_time))
            raise

    def equal_mysql_assert(self, value):
        """
        数据库相等断言，兼容SQL在键或值中的不同情况
        :param value: 预期结果，可能是{SQL: 预期值}或{预期值: SQL}
        :return: 返回flag标识，0表示正常，非0表示测试不通过
        """
        flag = 0
        sql = None
        assert_value = None

        try:
            # 识别SQL位置（优先识别值中的SQL）
            k, v = list(value.items())[0]

            if isinstance(v, str) and v.strip().upper().startswith("SELECT"):
                # 情况1: {实际值: SQL}
                sql = v
                assert_value = k
            elif isinstance(k, str) and k.strip().upper().startswith("SELECT"):
                # 情况2: {SQL: 预期值}
                sql = k
                assert_value = v
            else:
                flag += 1
                logs.error("数据库断言失败：未识别到有效的SQL语句")
                allure.attach(f"输入数据: {value}", 'SQL识别失败',
                              attachment_type=allure.attachment_type.TEXT)
                return flag

            # 执行数据库查询
            conn = ConnectMysql()
            db_value = conn.query_all(sql)

            if db_value is None:
                flag += 1
                logs.error("数据库断言失败：查询结果为空")
                allure.attach(f"SQL: {sql}\n预期值: {assert_value}\n实际值: None",
                              '数据库断言结果',
                              attachment_type=allure.attachment_type.TEXT)
                return flag

            # 处理查询结果（只取单列值）
            actual_values = []
            for row in db_value:
                if len(row) >= 1:  # 确保至少有一列数据
                    actual_values.append(str(row[0]))

            # 处理非sql的值（兼容字符串和列表）
            if isinstance(assert_value, str):
                # 移除可能的空格并分割
                expected_values = [x.strip() for x in assert_value.split(',')]
            elif isinstance(assert_value, list):
                expected_values = [str(x) for x in assert_value]
            else:
                expected_values = [str(assert_value)]

            # 比较实际值和预期值
            if actual_values == expected_values:
                logs.info(f"断言成功\nSQL: {sql}\n预期: {expected_values}\n实际: {actual_values}")
                allure.attach(f"SQL: {sql}\n预期值: {expected_values}\n实际值: {actual_values}",
                              '数据库断言：成功',
                              attachment_type=allure.attachment_type.TEXT)
            else:
                flag += 1
                logs.error(f"断言失败\nSQL: {sql}\n预期: {expected_values}\n实际: {actual_values}")
                allure.attach(f"SQL: {sql}\n预期值: {expected_values}\n实际值: {actual_values}",
                              '数据库断言：失败',
                              attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            flag += 1
            logs.error(f"数据库断言异常：{str(e)}\nSQL: {sql if sql else '未识别'}")
            allure.attach(f"异常信息: {str(e)}\nSQL: {sql if sql else '未识别'}",
                          '数据库断言异常',
                          attachment_type=allure.attachment_type.TEXT)

        return flag

    def status_code_eq_assert(self, assert_value, status_code):
        flag = 0
        if assert_value != status_code:
            flag += 1
            allure.attach(f"预期结果：{assert_value}\n实际结果：{status_code}", '响应代码断言结果:失败',
                          attachment_type=allure.attachment_type.TEXT)
            logs.error("接口返回码包含断言失败：接口返回码【%s】不等于【%s】" % (status_code, assert_value))
        else:
            allure.attach(f"预期结果：{assert_value}\n实际结果：{status_code}", '响应代码断言结果:成功',
                          attachment_type=allure.attachment_type.TEXT)
            logs.info("接口返回码包含断言成功：预期结果【%s】,实际结果【%s】" % (status_code, assert_value))
        return flag

    def status_code_neq_assert(self, assert_value, status_code):
        flag = 0
        if assert_value != status_code:
            allure.attach(f"预期结果：{assert_value}\n实际结果：{status_code}", '响应代码断言结果:成功',
                          attachment_type=allure.attachment_type.TEXT)
            logs.info("接口返回码包含断言成功：预期结果【%s】,实际结果【%s】" % (status_code, assert_value))

        else:
            flag += 1
            allure.attach(f"预期结果：{assert_value}\n实际结果：{status_code}", '响应代码断言结果:失败',
                          attachment_type=allure.attachment_type.TEXT)
            logs.error("接口返回码包含断言失败：接口返回码【%s】等于【%s】" % (status_code, assert_value))
        return flag
    def assert_result(self, expected, response, status_code):
        """
        断言，通过断言all_flag标记，all_flag==0表示测试通过，否则为失败
        :param expected: 预期结果
        :param response: 实际响应结果
        :param status_code: 响应code码
        :return:
        """
        all_flag = 0
        try:
            logs.info("yaml文件预期结果：%s" % expected)
            # logs.info("实际结果：%s" % response)
            # all_flag = 0
            for yq in expected:
                for key, value in yq.items():
                    if key == "contains":
                        flag = self.contains_assert(value, response, status_code)
                        all_flag = all_flag + flag
                    elif key == "eq":
                        flag = self.equal_assert(value, response, status_code)
                        all_flag = all_flag + flag
                    elif key == 'neq':
                        flag = self.not_equal_assert(value, response, status_code)
                        all_flag = all_flag + flag
                    elif key == 'eq_db':
                        flag = self.equal_mysql_assert(value)
                        all_flag = all_flag + flag
                    else:
                        logs.error("不支持此种断言方式")

        except Exception as exceptions:
            logs.error('接口断言异常，请检查yaml预期结果值是否正确填写!')
            raise exceptions

        if all_flag == 0:
            logs.info("测试成功")
            assert True
        else:
            logs.error("测试失败")
            assert False
