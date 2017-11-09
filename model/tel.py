import requests
from bs4 import BeautifulSoup
import re
from utils.log import logging

HOST = 'wlan.ct10000.com'
URL = 'http://wlan.ct10000.com'

HEADERS = {
    'Host': HOST,
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4'
}


def get_params():
    logging.info('Get http://www.example.com')
    res = requests.get('http://www.example.com')
    soup = BeautifulSoup(res.text, "html.parser")
    index_url = URL + soup.find_all('frame')[1]['src']
    HEADERS['Referer'] = res.url
    logging.info('Get {}'.format(index_url))
    index = requests.get(index_url, headers=HEADERS)
    index_soup = BeautifulSoup(index.text, "html.parser")
    user_dict = dict()
    for input_element in index_soup.find_all('input'):
        try:
            user_dict[input_element['name']] = input_element['value']
        except:
            try:
                user_dict[input_element['name']] = ''
            except:
                pass
    return user_dict, index.url


def wifi_portal_login(username, password):
    url = URL + '/authServlet'
    contents, ref = get_params()
    contents['UserName'] = username
    contents['PassWord'] = password
    HEADERS['Referer'] = ref
    logging.info('Post {}'.format(url))
    logging.debug('Contents: {}'.format(str(contents)))
    r = requests.post(url, headers=HEADERS, data=contents)
    if re.search('login_fail', r.text):
        error_msg = re.findall('\n\t\t\t(.*)<br />', r.text)[0]
        raise Exception('Login Failed', error_msg)
