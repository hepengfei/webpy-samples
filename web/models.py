# -*- coding:utf-8 -*-
import web

db = web.database(dbn='mysql', user='root', pw='', db='test', 
                  charset=None) # set charset to None 禁止web.database自动转换字符编码

def get_user_list():
    return db.select('username')
