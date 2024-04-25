#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from json import loads as json_loads
from time import sleep
from urllib import parse, request
from urllib.request import urlopen

from config import read_cfg


cfg = read_cfg()

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': parse.quote(cfg['cookie']),
    'Host': cfg['url']['server'].replace('http://', '').replace('https://', ''),
    'Origin': cfg['url']['server'],
}

headers |= cfg['headers']
login_data = cfg['login_data']
logout_data = cfg['logout_data']


def test_internet(host: str = 'http://connect.rom.miui.com/generate_204', timeout: int = 1) -> bool:
    """测试网络通断状态

    Args:
        host(str): 用于测试连接状态的generate_204服务器地址
        timeout(int): 超时时间（单位：秒）

    Returns:
        bool: True表示连接正常，False表示连接异常
    """

    try:
        resp = urlopen(host, timeout=timeout)
        if host.endswith('generate_204'):
            return resp.status == 204
        elif 200 <= resp.status <= 208 or resp.status == 226:
            return True
        return False
    except:  # noqa
        return False


def disconnect():
    """当目前已联网时要执行的操作"""

    resp = request.Request(
        cfg['url']['server'] + cfg['url']['logout'],
        data=bytes(parse.urlencode(login_data).encode('utf-8')),
        headers=headers,
        origin_req_host=None,
        unverifiable=False,
        method='POST',
    )

    try:
        res = request.urlopen(resp, timeout=10)
    except Exception as e:
        error_message = f'出现错误:\n{str(e)}'
        print('未知错误:', error_message)
        sys.exit(1)
    else:
        status = json_loads(res.read().decode())
        if status['result'] == 'success':
            print('断网成功！')
        elif status['result'] == 'fail':
            print('断网失败:\n',status["message"])
        else:
            print('未知错误:',status)


def connect():
    """当目前没有联网时要执行的操作"""

    resp = request.Request(
        cfg['url']['server'] + cfg['url']['login'],
        data=bytes(parse.urlencode(login_data).encode('utf-8')) if login_data else None,
        headers=headers,
        origin_req_host=None,
        unverifiable=False,
        method='POST',
    )

    try:
        res = request.urlopen(resp, timeout=10)
    except Exception as e:
        print('出现错误:\n',str(e))
        sys.exit(1)
    else:
        status = json_loads(res.read().decode())
        if status['result'] == 'success' and status['message'] == '':
            print('网络已连接！')
        elif status['result'] == 'success':
            print('联网成功')
        elif status['result'] == 'fail':
            print('未知错误:\n',status["message"])
        else:
            print('未知错误:\n',status)


def main():
    # 通过是否能连接到校园网登录服务器判断当前网络环境是否在校园网内
    if cfg['funtion']['check_school_network'] and not test_internet(
        host=cfg['url']['server'], timeout=3
    ):
        print('当前不在校园网环境，10s后重新检测\n若您的系统刚启动，可能还没反应过来，没有连上任何网络，为正常现象')
        sleep(10)
        if not test_internet(host=cfg['url']['server'], timeout=2):
            print('当前不在校园网环境，不自动尝试联网，程序自动退出')
            sys.exit(0)
    if test_internet():
        if cfg['funtion']['disconnect_network']:
            disconnect()
            sys.exit(0)
        else:
            print('网络本来就是通的噢~')
            sys.exit(0)
    connect()


if __name__ == '__main__':
    main()
