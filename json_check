# -*- coding:utf-8 -*-
'''
Created on Nov 16, 2018

'''
import json

def json_check(myjson):
    '''
           用于判断一个字符串是否符合Json格式
    :param self:
    :return:
    '''
    if isinstance(myjson, str):
        try:
            json.loads(myjson)
        except ValueError:
            return False
        return True
    else:
        return False

json1 = 'hello'
json2 = {'name':'xuyan'}
json3 = {"name":"panxi"}
json4 = json.dumps(json3)
print(json_check(json1))
print(json_check(json2))
print(json_check(json4))
