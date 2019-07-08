#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

import requests

"""
info:
author:CriseLYJ
github:https://github.com/CriseLYJ/
update_time:2019-04-04
"""

"""
模拟登陆豆瓣
"""


class YnLogin(object):
    def __init__(self, account, password):
        self.url = "http://120.77.169.160:7006/portal2/login"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*"
        }
        """初始化数据"""
        self.data = json.dumps({
            'password': password,
            'username': account
        })
        self.session = requests.Session()

    def get_cookie(self):
        """模拟登陆获取cookie"""
        html = self.session.post(url=self.url, headers=self.headers, data=self.data)
        response = html.text
        print(response)
        if json.loads(response)["success"]:
            print("恭喜你，登陆成功")

    def get_user_data(self):
        """获取用户数据表明登陆成功"""
        # TODO: 这里填写你用户主页的url
        url = "http://120.77.169.160:7006/#/user/person/detail/b4810b21f20c4546ac09829c56a14c70"
        # 获取用户信息页面
        html = self.session.get(url).text
        print(html)

    def run(self):
        """运行程序"""
        self.get_cookie()
        self.get_user_data()


if __name__ == '__main__':
    # account = input("请输入你的账号:")
    # password = input("请输入你的密码:")
    account = 'linxiaobin1'
    password = '123456'
    login = YnLogin(account, password)
    login.run()
