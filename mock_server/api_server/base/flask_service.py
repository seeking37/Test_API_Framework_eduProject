# -*- coding: utf-8 -*-
import datetime
import math
import string
import time
from hashlib import sha1
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_jwt_extended import set_access_cookies
import os
import sys
import re
from datetime import datetime as dt

# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取项目的根目录
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

# from mock_server.api_server.confs.setting import DIR_BASE  # noqa: E402
from confs.setting import DIR_BASE


import flask  # noqa: E402
import json  # noqa: E402
import random  # noqa: E402
from flask import jsonify, make_response, request  # noqa: E402
from functools import wraps  # noqa: E402

"""
mock接口服务
"""

# __name__表示当前的python文件名，把该文件当做一个服务
api = flask.Flask(__name__)

api.config.from_object(__name__)
# 定义Flask app时，指定JSON_AS_ASCII的参数设置为False，阻止jsonify将json内容转为ASCII进行返回
api.config['JSON_AS_ASCII'] = False

global_params = {}

api.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(api)

mer_is = []


def read_data(file_path):
    with open(file_path, 'r', encoding='GBK') as f:
        data = f.read()
        return data


def read_json_data(file_path):
    """json文件读取"""
    with open(file_path, 'r', encoding='utf-8') as f:
        result = ''.join([line.strip() for line in f])
        mer = result.split(',')
        return mer


def write_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data)


def timestamp():
    """获取当前时间戳，10位"""
    t = int(time.time())
    return t


def now_date():
    """获取当前时间标准时间格式"""
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return now_time


def timestamp_thirteen():
    """获取当前的时间戳，13位"""
    t = int(time.time()) * 1000
    return t

def start_time():
    """获取当前时间的后一天标准时间"""
    now_time = datetime.datetime.now()
    one_day_delta = datetime.timedelta(days=1)
    day_before_time = (now_time + one_day_delta).strftime("%Y-%m-%d %H:%M:%S")
    return day_before_time

def end_time():
    """获取当前时间的后三天标准时间"""
    now_time = datetime.datetime.now()
    three_days_delta = datetime.timedelta(days=3)
    day_before_time = (now_time + three_days_delta).strftime("%Y-%m-%d %H:%M:%S")
    return day_before_time

def sha1_encryption(params):
    """参数sha1加密"""
    enc_data = sha1()
    # 获取待输出数据
    enc_data.update(params.encode(encoding="utf-8"))
    return enc_data.hexdigest()

# 设置post表单json提交请求头装饰器
def set_headers(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        response = make_response(func(*args, **kwargs))
        response.headers['Content-Type'] = 'application/json;charset=UTF-8'
        response.headers['token'] = global_params['token']
        return response

    return decorated_function

# ========================================================================================================================


@api.route('/ssm_web/user/findAllUserByPage', methods=['post'])
def find_all_users():
    """用户分页查询接口"""
    # 读取用户数据
    data = read_data(DIR_BASE + '/data/mockdata/user.json')
    users = json.loads(data)['RECORDS']

    # 获取请求参数
    request_data = request.get_json()
    if not request_data or request_data=='null':
        return jsonify({
            'message': '请求参数不能为空',
            'success': False
        }),400
    
    # 验证必填参数
    current_page = request_data.get('currentPage')
    page_size = request_data.get('pageSize')
    
    if not current_page and current_page != 0:
        return jsonify({
            'message': '缺少必填参数currentPage',
            'success': False
        }),400
    
    if not page_size and page_size != 0:
        return jsonify({
            'message': '缺少必填参数pageSize',
            'success': False
        }),400
    
    # 验证参数类型
    try:
        current_page = int(current_page)
        page_size = int(page_size)
    except ValueError:
        return jsonify({
            'message': '参数类型错误，currentPage和pageSize必须为整数',
            'success': False
        }),400
    
    # 验证参数范围
    if current_page < 1:
        return jsonify({
            'message': '页码必须大于0',
            'success': False
        }),400
    
    if page_size < 1:
        return jsonify({
            'message': '每页条数不能小于1',
            'success': False
        }),400
    
    # 获取搜索条件
    username = request_data.get('username')
    start_create_time = request_data.get('startCreateTime')
    end_create_time = request_data.get('endCreateTime')
    
    # 验证时间格式
    if start_create_time or end_create_time:
        try:
            if start_create_time:
                dt.strptime(start_create_time, '%Y-%m-%d')
            if end_create_time:
                dt.strptime(end_create_time, '%Y-%m-%d')
        except ValueError:
            return jsonify({
                'message': '时间格式错误，正确格式为：YYYY-MM-DD',

                'success': False
            }),400
    
    # 过滤数据
    filtered_users = []
    for user in users:
        # 用户名过滤
        if username:
            # 修改用户名匹配逻辑，使用精确匹配
            if username != user['name']:
                continue
        else:
            # 如果没有用户名搜索条件，保留所有记录
            pass
            
        # 时间范围过滤
        if start_create_time or end_create_time:
            user_create_time = datetime.strptime(user['create_time'], '%d/%m/%Y')
            if start_create_time:
                start_time = datetime.strptime(start_create_time, '%Y-%m-%d')
                if user_create_time < start_time:
                    continue
            if end_create_time:
                end_time = datetime.strptime(end_create_time, '%Y-%m-%d')
                if user_create_time > end_time:
                    continue
        
        filtered_users.append(user)
    
    # 计算分页信息
    total = len(filtered_users)
    # 修改分页计算逻辑：使用math.ceil确保向上取整
    # total_pages = math.ceil(total / page_size) if page_size > 0 else 0

    # 处理总页数（避免除零/空数据边界情况）
    total_pages = 0
    if total > 0:
        total_pages = 1 if page_size == 0 else math.ceil(total / page_size)
    else:
        total_pages = 1  # 即使无数据也保留1页（前端兼容）


    
    # 验证页码范围
    if current_page > total_pages and total_pages > 0:
        return jsonify({
            'message': f'页码超出范围，最大页码为{total_pages}',
            'success': False
        }),400
    
    # 分页处理
    start_idx = (current_page - 1) * page_size
    end_idx = start_idx + page_size
    page_users = filtered_users[start_idx:end_idx]
    
    # 构建响应
    response = {
        'message': '响应成功',
        'status_code': 200,
        'success': True,
        'content': {
            'list': page_users,
            'total': total,
            'pageNum': current_page,
            'pageSize': page_size,
            'size': len(page_users),
            'firstPage': 1,
            'lastPage': total_pages,
            'prePage': current_page - 1 if current_page > 1 else 0,
            'nextPage': current_page + 1 if current_page < total_pages else 0,
            'isFirstPage': current_page == 1,
            'isLastPage': current_page == total_pages,
            'hasPreviousPage': current_page > 1,
            'hasNextPage': current_page < total_pages
        }
    }
    
    return jsonify(response)


@api.route('/ssm_web/course/saveOrUpdateCourse', methods=['post'])
def save_or_update_course():
    """新增/修改课程接口"""
    # 验证Authorization头
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({
            'message': '缺少Authorization头',
            'success': False,
            'state': 401
        }), 401
    
    # 验证Authorization格式（简单验证）
    if auth_header == 'Bearer invalid_token_12345':
        return jsonify({
            'message': '无效的Authorization令牌',
            'success': False,
            'state': 401
        }), 401
    
    # 验证Content-Type
    content_type = request.headers.get('Content-Type', '')
    if not content_type.startswith('application/json'):
        return jsonify({
            'message': 'Content-Type必须为application/json',
            'success': False,
            'state': 400
        }), 400
    
    # 获取请求参数
    request_data = request.get_json()
    
    # 验证请求体不能为空
    if not request_data:
        return jsonify({
            'message': '请求参数不能为空',
            'success': False,
            'state': 400
        }), 400
    
    # 验证必填参数
    required_fields = ['brief', 'courseName', 'previewFirstField']
    for field in required_fields:
        if not request_data.get(field):
            return jsonify({
                'message': f'缺少必填参数：{field}',
                'success': False,
                'state': 400
            }), 400
    
    # 验证课程名称长度
    course_name = request_data.get('courseName')
    if len(course_name) > 50:
        return jsonify({
            'message': '课程名称长度不能超过50个字符',
            'success': False,
            'state': 400
        }), 400
    
    # 验证价格格式
    price = request_data.get('price')
    if price is not None:
        try:
            price_float = float(price)
            if price_float < 0:
                return jsonify({
                    'message': '价格不能为负数',
                    'success': False,
                    'state': 400
                }), 400
        except (ValueError, TypeError):
            return jsonify({
                'message': '价格格式错误',
                'success': False,
                'state': 400
            }), 400
    
    # 判断是新增还是修改
    course_id = request_data.get('id')
    is_update = course_id and course_id.strip()
    
    if is_update:
        # 修改课程逻辑
        try:
            course_id_int = int(course_id)
        except (ValueError, TypeError):
            return jsonify({
                'message': '课程ID格式错误',
                'success': False,
                'state': 400
            }), 400
        
        # 模拟检查课程是否存在
        if course_id_int == 999999:
            return jsonify({
                'message': '课程不存在',
                'success': False,
                'state': 404
            }), 404
        
        # 修改成功响应
        response_data = {
            'success': True,
            'state': 200,
            'message': '响应成功',
            'content': {
                'id': course_id_int,
                'courseName': request_data.get('courseName'),
                'brief': request_data.get('brief'),
                'price': float(request_data.get('price', 0)),
                'previewFirstField': request_data.get('previewFirstField'),
                'previewSecondField': request_data.get('previewSecondField'),
                'updateTime': timestamp_thirteen()
            }
        }
    else:
        # 新增课程逻辑
        new_course_id = random.randint(1000, 9999)
        
        response_data = {
            'success': True,
            'state': 200,
            'message': '响应成功',
            'content': {
                'id': new_course_id,
                'courseName': request_data.get('courseName'),
                'brief': request_data.get('brief'),
                'price': float(request_data.get('price', 0)),
                'priceTag': request_data.get('priceTag'),
                'discounts': float(request_data.get('discounts', 0)),
                'discountsTag': request_data.get('discountsTag'),
                'courseDescriptionMarkDown': request_data.get('courseDescriptionMarkDown', ''),
                'courseDescription': request_data.get('courseDescription'),
                'courseImgUrl': request_data.get('courseImgUrl', ''),
                'isNew': int(request_data.get('isNew', 0)),
                'isNewDes': request_data.get('isNewDes'),
                'lastOperatorId': 0,
                'autoOnlineTime': None,
                'createTime': timestamp_thirteen(),
                'updateTime': timestamp_thirteen(),
                'isDel': 0,
                'totalDuration': 0,
                'courseListImg': request_data.get('courseListImg', ''),
                'status': int(request_data.get('status', 0)),
                'sortNum': int(request_data.get('sortNum', 0)),
                'previewFirstField': request_data.get('previewFirstField'),
                'previewSecondField': request_data.get('previewSecondField'),
                'sales': int(request_data.get('sales', 0)),
                'teacherName': request_data.get('teacherName'),
                'position': request_data.get('position'),
                'description': request_data.get('description'),
                'activityCourse': request_data.get('activityCourse', False)
            }
        }
    
    return jsonify(response_data)


@api.route('/login', methods=['get'])
def set_cookie():
    """设置cookie"""
    resp = make_response("")
    randoms = ''.join([random.choice(string.hexdigits) for i in range(20)])
    cookie_value = sha1_encryption(randoms)
    resp.set_cookie('Cookie', cookie_value, max_age=60 * 60 * 24)
    return resp

if __name__ == '__main__':
    # debug=True，改代码后不用重启，会自动重启
    print(DIR_BASE) # 输出为C:\tocode\Project\cursor\Test_API_Framework\mock_server\api_server
    print(project_root)
    api.run(host='127.0.0.1', port=8787, debug=True)

