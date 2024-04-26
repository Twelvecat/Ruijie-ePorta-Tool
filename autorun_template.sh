#!/bin/bash

# 可以将此脚本添加到crontab自动执行或者添加到开启自启，基本逻辑是先判断是否联网在判断是否执行减少其他网络环境下的重复调用

# 尝试ping 8.8.8.8
ping -c 1 8.8.8.8 > /dev/null 2>&1
ping_status=$?

# 根据ping命令的返回状态处理不同的情况
if [ $ping_status -eq 0 ]; then
    echo "OK: Ping succeeded"
    exit 0
elif [ $ping_status -ne 0 ]; then
    echo "CRITICAL: Ping check failed"
    echo "Try to detect the network environment"
    # 启动一个程序，此处的路径可以更具实际情况修改，可能会是绝对路径
    python ./src/__main__.py &
    exit 1
else
    echo "UNKNOWN: Something went wrong"
    echo "Try to detect the network environment"
    # 启动相同的程序，此处的路径可以根据实际使用情况修改，可能会是绝对路径
    python ./src/__main__.py &
    exit 3
fi
