import sys
from conf import setting
import logging
import os
import time
from logging.handlers import RotatingFileHandler  # 按文件大小滚动备份
import datetime

log_path = setting.FILE_PATH["LOG"]
if not os.path.exists(log_path): 
    os.makedirs(log_path, exist_ok=True)  # 修改1: 使用makedirs确保目录创建

# 修改2: 使用os.path.join代替硬编码路径分隔符
logfile_name = os.path.join(log_path, "test.{}.logs".format(time.strftime("%Y%m%d")))


class RecordLog:
    """日志模块"""

    def __init__(self):
        # 修改3: 确保日志目录存在后再处理过期日志
        if not os.path.exists(log_path):
            os.makedirs(log_path, exist_ok=True)
        self.handle_overdue_log()

    def handle_overdue_log(self):
        """处理过期日志文件"""
        # 修改4: 首先确保目录存在
        if not os.path.exists(log_path):
            return
        
        # 获取系统的当前时间
        now_time = datetime.datetime.now()
        # 日期偏移30天，最多保留30的日志文件，超过自动清理
        offset_date = datetime.timedelta(days=-30)
        # 获取前一天时间戳
        before_date = (now_time + offset_date).timestamp()
        # 找到目录下的文件
        files = os.listdir(log_path)
        for file in files:
            # 修改5: 使用os.path.join代替硬编码路径分隔符
            filepath = os.path.join(log_path, file)
            if os.path.isfile(filepath):  # 添加文件类型检查
                try:
                    file_create_time = os.path.getctime(filepath)  # 获取文件创建时间,返回时间戳
                    if file_create_time < before_date:
                        os.remove(filepath)
                except FileNotFoundError:
                    # 文件可能已被删除，忽略错误
                    pass

    def output_logging(self):
        """获取logger对象"""
        logger = logging.getLogger(__name__)
        # 防止重复打印日志
        if not logger.handlers:
            logger.setLevel(setting.LOG_LEVEL)
            log_format = logging.Formatter(
                '%(levelname)s - %(asctime)s - %(filename)s:%(lineno)d -[%(module)s:%(funcName)s] - %(message)s')
            # 日志输出到指定文件，滚动备份日志
            fh = RotatingFileHandler(filename=logfile_name, mode='a', maxBytes=5242880,
                                     backupCount=7,
                                     encoding='utf-8')  # maxBytes:控制单个日志文件的大小，单位是字节,backupCount:用于控制日志文件的数量

            fh.setLevel(setting.LOG_LEVEL)
            fh.setFormatter(log_format)
            # 将相应的handler添加在logger对象中
            logger.addHandler(fh)

            # 输出到控制台
            sh = logging.StreamHandler()
            sh.setLevel(setting.STREAM_LOG_LEVEL)
            sh.setFormatter(log_format)
            logger.addHandler(sh)
        return logger


apilog = RecordLog()
logs = apilog.output_logging()