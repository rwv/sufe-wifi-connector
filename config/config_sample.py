"""
登陆信息配置文件
os: 操作系统 ('mac', 'windows', 'linux')
type: 网络类型 ('tel', "unicom', 'cmcc')
username: 网络账号
password: 登陆密码
interval: 心跳包间隔，默认值10，可不修改。
"""
login_config = {
    'type': 'unicom',
    'username': 'c2016091900000000',
    'password': '00000000',
}

other_config = {
    'os': 'mac',
    'interval': 10
}
