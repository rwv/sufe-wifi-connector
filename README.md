# sufe-wifi-connector
Shanghai University of Finance and Economics Wi-Fi connector

上海财经大学 Wi-Fi 自动登录

## 支持

|  | 电信 | 联通 | 移动 |
| :-: | :-: | :-: | :-: |
| Windows |  |  |  |
| macOS |  | √  |  |
| Linux |  |  |  |

联通在 macOS 10.13 上经过测试成功

## 使用方法

### macOS

首先修改 `config` 文件夹中的 `config_sample.py` 中的登录信息和电脑系统信息。

在终端中执行

```bash
$ pip install -r requirements.txt
$ python3 connector.py
```

## Contribute

* Use It
* Open Issue
* Send Pull Request

## TODO

* [ ] Windows
* [ ] Linux
* [ ] 电信
* [ ] 移动
* [ ] 针对 macOS 和 Linux 编写 `setup.sh`
* [ ] Travis-CI 和 Coveralls
* [ ] 针对 Windows 使用 py2exe 打包


