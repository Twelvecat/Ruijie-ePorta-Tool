#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import sys
from tkinter import Tk, messagebox

import requests

import rwjson

# 使编译器能正确导入ico文件
if getattr(sys, 'frozen', None):
    basedir = sys._MEIPASS
else:
    basedir = os.path.dirname(__file__)

win = Tk()
win.withdraw()  # 禁用tkinter主窗口
# 如果正确导入了ico文件则设置tkinter对话框图标
if os.path.exists(os.path.join(basedir, "wangluo.ico")):
    win.iconbitmap(os.path.join(basedir, "wangluo.ico"))


def connect_network():
    f = rwjson.read_json()
    url = f[0]['login_url']
    data = f[1]
    header = f[3]
    cookie = f[5]

    try:
        res = requests.post(url=url, data=data, headers=header, cookies=cookie)
    except Exception as e:
        print('错误：', e)
        error_message = '出现错误！\n错误信息：' + str(e)
        messagebox.showerror(title='未知错误', message=error_message)
        sys.exit(1)
    else:
        res.encoding = 'utf-8'
        print(res.text)
        json1 = json.loads(res.text)
        return json1


def disconnect_network():
    f = rwjson.read_json()
    url = f[0]['logout_url']
    data = f[2]
    header = f[4]

    try:
        res = requests.post(url=url, data=data, headers=header)
    except Exception as e:
        print('错误：', e)
        error_message = '出现错误！\n错误信息：' + str(e)
        messagebox.showerror(title='未知错误', message=error_message)
        sys.exit(1)
    else:
        res.encoding = 'utf-8'
        print(res.text)
        json1 = json.loads(res.text)
        return json1