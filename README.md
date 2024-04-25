# Ruijie-ePorta-Tool

本项目fork自[Redlnn/Ruijie-ePorta-Tool](https://github.com/Redlnn/Ruijie-ePorta-Tool)，原项目已不再更新，本分支会继续维护。

**本分支是专用于linux版本或不需要界面的windows版本，只保留了最基本的python代码。依赖比较少，不需要poetry进行管理（主要是我安装poetry时各种依赖报错，比较烦）。配置文件的方法和win一样。去掉了一些可视化的提示框，改成最简单的打印。**

一个基于 Python3 的自动登录/断开锐捷 ePorta Web 网页认证的工具（可开关功能，理论支持大部分学校）

<img src="./example.png" alt="锐捷 ePorta Web 网页认证界面（webp图片无法打开请切换浏览器）" width="500px">

<h4>权责声明</h4>

- 本程序仅供研究学习之用，无意对锐捷的认证机制做任何抵触性行为
- 本程序不可用于任何商业和不良用途，否则责任自负
- 本程序不保证在任何环境下能够通过，本人也不保证能按时按网友要求改进本程序，其编写及维护纯属个人爱好，有可能被随时终止
- 本程序不保证经过严格测试对机器无害，由于未知的使用环境或不当的使用对计算机造成的损害，责任由使用者全部承担
- 由于任何不遵守上叙条例引起的纠纷，均与本人无关

## 简介

通过 urllib 标准库来发送 POST 请求实现锐捷 ePortal Web 认证的登录/下线功能

理论上支持已安装 Python3 的 Windows、Linux、MacOS 等操作系统

## 特性

- 运行时自动判断网络通断，网络通则询问是否需要断网（可在配置文件中关闭该功能，关闭后网络通时自动退出），网络不通则尝试进行联网
- 运行时自动判断当前连接的网络是否是校园网（可在配置文件中关闭该功能）
- 可根据配置文件内容动态调整登录/下线时使用的 登陆页面、HTML Header、传递的参数、cookie
- 理论上可适配所有登录不需要验证码的学校

## 使用方法

如果获取配置文件所需内容即配置方法请看 👉 [B站视频](https://www.bilibili.com/video/BV1TZ4y167b6/)

配置文件中 `Cookie`、`login_data` 与 `logout_data` 的内容均需要根据校园网服务器动态调整，
不够就加，多了就删除（希望你能明白怎么填，不明白我也没办法教你）

在部分学校，不管是哪个参数，即使错了 1 个字，都可能导致禁止登录 3-5 分钟，用钱请自行斟酌风险

- Windows 用请从[Releases](https://github.com/Redlnn/Ruijie-ePorta-Tool/releases)处直接下载预构建版本
- MacOS / Linux 用户请自行使用源代码直接运行或打包使用

默认只发布 Windows 构建，MacOS和Linux可以直接使用源代码或自行打包使用

如需开机启动，Windows下只需创建一个快捷方式并将其放到 `%appdata%\Microsoft\Windows\Start Menu\Programs\Startup` 文件夹中（复制该地址到资源管理器窗口的地址栏回车即可）

### Tips

- 使用 Wi-Fi 连接校园网则建议关闭随机 MAC 地址
  > Windows 10/11 系统中该选项位于：系统设置 - 网络和 Internet - WLAN - 管理已知网络 - <你所在学校的校园网无线 SSID> - 属性 - 对此网络使用随机地址
- 如需开机启动可创建快捷方式/符号链接（软链接）并复制到启动目录
- 可以通过关闭断网功能并添加至任务计划以定期检查防止设备断网 (commit 6e630ff中该功能的表现与之前不同，关闭断网功能后不再判断设备是否联网，每次启动本程序都将尝试联网)

## Build 构建

1. clone 本仓库
2. 使用 `poetry` 安装依赖（有关 Poetry 是什么或怎么用请看[他们官网](https://python-poetry.org/docs/)）
3. Windows 直接双击运行 `build.bat` （支持 upx 压缩）
4. 待命令执行完毕后可在 `dist` 文件夹找到构建好的 exe 文件

## 局限性

- 锐捷 ePortal Web 认证的 POST 数据包中存在 `validcode` 参数，这个参数应该是图形验证码。我所在的学校并没有开启验证码，只有在登录尝试次数过多的时候才会出现验证码。如果你的学校在登录的时候需要验证码，那么本程序将无法进行认证。
- 本人是 Python 初学者，代码冗余杂乱，可能运行效率不高。
