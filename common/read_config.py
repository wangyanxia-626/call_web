# -*- coding:utf-8 -*-
# @Time :2020-03-23 19:43
# @Email :876417305@qq.com
# @Author :yanxia
# @File :read_config.PY
import configparser
from common import file_adress
class ReadConfig:
    '''完成配置文件的读取'''
    def __init__(self):
        #实例化ConfigParser()这个类
        self.config=configparser.ConfigParser()
        #获取这个总开关，确定是跑线上数据还是测试数据
        self.config.read(file_adress.global_file)
        switch=self.config.getboolean("switch","on")
        #如果开关打开为True，使用online数据，为False跑测试数据
        if switch:
            self.config.read(file_adress.online_file)
        else:
            self.config.read(file_adress.test_file)
    def get(self,section,option):
        return self.config.get(section,option)

config=ReadConfig()

# if __name__ == '__main__':
#     config=ReadConfig()
#     print(config.get("switch","on"))

