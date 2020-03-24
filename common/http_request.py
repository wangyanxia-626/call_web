# -*- coding:utf-8 -*-
# @Time :2020-03-23 17:42
# @Email :876417305@qq.com
# @Author :yanxia
# @File :http_request.PY
from common.read_config import config
from common import logger
import requests

logger=logger.get_logger(__name__)
'''封装request请求，不需要传cookies的写法，利用session对象，自动传递cookies'''
class HttpRequest:
    def __init__(self):
        self.session=requests.sessions.session()
    def request(self,method,url,data=None,json=None):
        if type(data)==str:
            data=eval(data)
        #拼接请求的url
        url=config.get('URL','web_url')+url
        logger.debug("请求的url{}".format(url))
        logger.debug("请求的data{}".format(data))
        try:
            if method.lower()=='get':
                res=self.session.request(method=method,url=url,params=data)
            elif method.lower()=='post':
                if json:
                    res=self.session.request(method=method,url=url,json=json)
                else:
                    res=self.session.request(method=method,url=url,data=data)
            else:
                res=None
                logger.error("不支持的请求方法")
        except Exception as e:
            logger.error("请求报错了{}".format(e))
            raise e
        return res
    def close(self):
        self.session.close()

if __name__ == '__main__':
    http_request = HttpRequest()
    params = {"username":"zhuge2019","password":'QAZwsx123'}
    resp = http_request.request("post","/home/index/index", data=params)
    print(resp.json())

