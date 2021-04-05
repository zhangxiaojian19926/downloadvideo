# -*- coding: utf-8 -*-
import functools

# 用户名登录模块
def login_in(origin):
    @functools.wraps(origin)
    def inner():
        while True:
            username = input("username:")
            password = input("password:")
            if username != "zhang" or password != "1234":
                print("username or password is wrong")
                continue
            else:
                origin()
                break

    return inner
