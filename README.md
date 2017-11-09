# sufe-wifi-connector
Shanghai University of Finance and Economics Wi-Fi connector

上海财经大学 Wi-Fi 自动登录

## 支持

|  | 电信 | 联通 | 移动 |
| :-: | :-: | :-: | :-: |
| Windows |  |  |  |
| macOS |  | √ | √ |
| Linux |  | √ | √ |


注：

1. 联通在 macOS 10.13 上经过测试成功
1. Linux 未测试
1. 移动未测试（似乎登陆逻辑和联通一样）

## 使用方法

### macOS

首先修改 `config` 文件夹中的 `config_sample.py` 中的登录信息和电脑系统信息。

在终端中执行

```bash
$ pip3 install -r requirements.txt
$ python3 connector.py
```

### Linux

首先修改 `config` 文件夹中的 `config_sample.py` 中的登录信息和电脑系统信息。

在终端中执行

```bash
$ pip3 install -r requirements.txt
$ python3 connector.py
```

## Contribute

* Use It
* Open Issue
* Send Pull Request

## TODO

* [ ] Windows
* [x] Linux
* [ ] 电信
* [x] 移动
* [ ] 针对 macOS 和 Linux 编写 `setup.sh`
* [ ] Travis-CI 和 Coveralls
* [ ] 针对 Windows 使用 py2exe 打包
* [x] Log


