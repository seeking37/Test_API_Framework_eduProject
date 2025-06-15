import os
import time
from datetime import datetime
from common.connection import ConnectMysql, ConnectRedis, ConnectMongo
from common.recordlog import logs
from conf.operationConfig import OperationConfig
from conf.setting import FILE_PATH
class MysqlManager:
    """数据管理类，用于处理数据的备份、还原和初始化"""
    
    def __init__(self):
        self.mysql = ConnectMysql()
        self.conf = OperationConfig()
        self.backup_dir = FILE_PATH['BACKUP']
        
        # 创建备份目录
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
    
    def backup_data(self, table_name=None):
        """备份MySQL数据
        
        Args:
            table_name (str, optional): 要备份的表名，如果为None则备份整个数据库
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = os.path.join(self.backup_dir, f"mysql_backup_{timestamp}.sql")
            
            mysql_exe_command = "mysqldump"
            table_param = f" {table_name}" if table_name else ""
            
            sql = f"{mysql_exe_command} -u {self.conf.get_section_mysql('username')} " \
                  f"-p{self.conf.get_section_mysql('password')} " \
                  f"-P {self.conf.get_section_mysql('port')} " \
                  f"-h {self.conf.get_section_mysql('host')} " \
                  f"{self.conf.get_section_mysql('database')}{table_param} > {backup_file}"
            
            logs.info(f"执行MySQL备份命令")
            # logs.info(f"执行MySQL备份命令: {sql}")
            os.system(sql)
            return backup_file
            
        except Exception as e:
            logs.error(f"MySQL数据备份失败: {str(e)}")
            raise
    
    def restore_data(self, backup_file):
        """还原MySQL数据
        
        Args:
            backup_file (str): 备份文件路径
        """
        try:
            mysql_exe_command = "mysql"
            sql = f"{mysql_exe_command} -u {self.conf.get_section_mysql('username')} " \
                  f"-p{self.conf.get_section_mysql('password')} " \
                  f"-P {self.conf.get_section_mysql('port')} " \
                  f"-h {self.conf.get_section_mysql('host')} " \
                  f"{self.conf.get_section_mysql('database')} < {backup_file}"
            
            # logs.info(f"执行MySQL还原命令: {sql}")
            logs.info(f"执行MySQL还原命令")
            os.system(sql)
            
        except Exception as e:
            logs.error(f"MySQL数据还原失败: {str(e)}")
            raise
    
    def init_data(self, init_file):
        """初始化MySQL数据
        
        Args:
            init_file (str): 初始化SQL文件路径
        """
        try:
            mysql_exe_command = "mysql"
            sql = f"{mysql_exe_command} -u {self.conf.get_section_mysql('username')} " \
                  f"-p{self.conf.get_section_mysql('password')} " \
                  f"-P {self.conf.get_section_mysql('port')} " \
                  f"-h {self.conf.get_section_mysql('host')} " \
                  f"{self.conf.get_section_mysql('database')} < {init_file}"
            
            # logs.info(f"执行MySQL数据初始化命令: {sql}")
            logs.info(f"执行MySQL数据初始化命令")
            os.system(sql)
            
        except Exception as e:
            logs.error(f"MySQL数据初始化失败: {str(e)}")
            raise

if __name__ == '__main__':
    mysql_manager = MysqlManager()
    backup_file = None
    # 1. 备份数据
    backup_file = mysql_manager.backup_data("course")
    # 2. 初始化测试数据
    mysql_manager.init_data('../backup/init_course.sql')
    # 4. 还原数据
    if backup_file:
        mysql_manager.restore_data(backup_file)