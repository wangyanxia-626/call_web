# -*- coding:utf-8 -*-
# @Time :2020-03-23 20:56
# @Email :876417305@qq.com
# @Author :yanxia
# @File :logger.PY
import logging
from common import file_adress
from common.read_config import config
def get_logger(name):
    logger=logging.getLogger(name)
    logger.setLevel('DEBUG')
    formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-日志信息：%(message)s-[%(filename)s:%(lineno)d]")

    #设置输出到控制台
    console_handler=logging.StreamHandler()
    console_level=config.get('logger','console_level')
    console_handler.setLevel(console_level)
    console_handler.setFormatter(formatter)

    #设置输出到配置文件
    file_handler=logging.FileHandler(file_adress.log_dir + '/cases.log', encoding='utf-8')
    file_level=config.get('logger','file_level')
    file_handler.setLevel(file_level)
    file_handler.setFormatter(formatter)
    #关联
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    #关闭输出
    logger.removeHandler(console_handler)
    logger.removeHandler(file_handler)
    return logger
