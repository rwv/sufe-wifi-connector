import base64

import requests
from bs4 import BeautifulSoup

HEADERS = {
    'Host': '202.121.129.151:8080',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'DNT': '1',
    'Referer': r'http://202.121.129.151:8080/portal/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
}


def get_params():
    url = r'http://202.121.129.151:8080/portal/index_custom11.jsp'
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text)
    user_dict = dict()
    for input_element in soup.find_all('input'):
        try:
            user_dict[input_element['name']] = input_element['value']
        except:
            continue
    user_dict.pop('login')
    user_dict.pop('logout')
    return user_dict, res.cookies


def connect_to_wifi(username, password):
    url = r'http://202.121.129.151:8080/portal/pws?t=lo'
    contents, cookies = get_params()
    contents['userName'] = username
    contents['userPwd'] = base64.b64encode(password.encode()).decode('ascii')
    r = requests.post(url, data=contents, headers=HEADERS, cookies=cookies)
