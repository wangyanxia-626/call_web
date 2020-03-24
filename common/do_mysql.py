# -*- coding:utf-8 -*-
# @Time :2020-03-24 8:23
# @Email :876417305@qq.com
# @Author :yanxia
# @File :do_mysql.PY
import pymysql
from common.read_config import ReadConfig
class DoMysql:
    '''完成数据库的交互封装'''
    def __init__(self):
        #读取配置文件里面的数据库信息
        my_sql=eval(ReadConfig().get('DB','db_config'))
        self.mysql=pymysql.connect(**my_sql)
        #创建游标的时候创建一个字典类型的游标
        self.cursor=self.mysql.cursor(pymysql.cursors.DictCursor)

    def fetch_one(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()
    def fetch_all(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchall()
    def fetch_many(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchmany()
    def close(self):
        self.cursor.close()
        self.mysql.close()

if __name__ == '__main__':
    print(DoMysql().mysql)

