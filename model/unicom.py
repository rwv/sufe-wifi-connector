import base64
import json
import time

import requests
from bs4 import BeautifulSoup

from utils.log import logging

HOST = '202.121.129.151:8080'
URL = 'http://202.121.129.151:8080'
HEADERS = {
    'Host': HOST,
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'DNT': '1',
    'Referer': URL + '/portal/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4'
}


def get_params():
    """
    get the params from the web page

    :returns: a dict of params got from the web page content, cookies
    """
    url = URL + '/portal/index_custom11.jsp'
    logging.info('Get {}'.format(url))
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")
    user_dict = dict()
    for input_element in soup.find_all('input'):
        try:
            user_dict[input_element['name']] = input_element['value']
        except:
            continue
    user_dict.pop('login')
    user_dict.pop('logout')
    logging.debug(user_dict)
    return user_dict, res.cookies


def json_url_decode(text):
    """
    Decode the serialized and base64 string of json

    :param text: serialized and base64 string of json
    :return: the decode content of parsed json
    """
    data = text.encode()
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'=' * (4 - missing_padding)
    return json.loads(requests.utils.unquote(base64.b64decode(data).decode('ascii')))


def do_heartbeat(portal_link, cookies):
    """
    do the heartbeat

    :param portal_link: the portal link fetched in the login process
    :param cookies: cookies
    """
    url = URL + '/portal/page/doHeartBeat.jsp?pl={}'.format(portal_link)
    res_json = json_url_decode(portal_link)
    contents = {
        'user_ip': res_json['clientPrivateIp'],
        'bas_ip': res_json['nasIp'],
        'userDevPort': res_json['userDevPort'],
        'userStatus': res_json['userStatus'],
        'serialNo': res_json['serialNo'],
        'language': res_json['clientLanguage'],
        'e_d': '',
        't': 'hb'
    }
    logging.info('Post {}'.format(URL + '/portal/page/doHeartBeat.jsp'))
    logging.info('Do heartbeat')
    logging.debug('Contents: {}'.format(str(res_json)))
    requests.post(url, data=contents, cookies=cookies, headers=HEADERS)


def do_logout(contents=None, cookies=None):
    """
    do the logout

    :param contents: the contents to logout, same as get_params()
    :param cookies: the cookies
    """
    if not contents:
        contents, cookies = get_params()
    url = URL + '/portal/pws?t=lo'
    logging.info('Post {}'.format(url))
    logging.debug('Contents: {}'.format(str(contents)))
    r = requests.post(url, data=contents, headers=HEADERS, cookies=cookies)
    logging.debug('Response: {}'.format(r.text))


def wifi_portal_login(username, password):
    """
    do the login

    :param username: username
    :param password: password
    :returns: (heartbeat function, logout function)
    """
    url = URL + '/portal/pws?t=li'
    contents, cookies = get_params()
    logout = lambda: do_logout(contents, cookies)
    contents['userName'] = username
    contents['userPwd'] = base64.b64encode(password.encode()).decode('ascii')
    logging.info('Post {}'.format(url))
    logging.debug('Contents: {}'.format(str(contents)))
    r = requests.post(url, data=contents, headers=HEADERS, cookies=cookies)
    logging.debug('Response: {}'.format(r.text))
    res_json = json_url_decode(r.text)
    logging.debug('Response decoded: {}'.format(str(res_json)))
    if res_json['errorNumber'] != '1':
        logging.debug(res_json)
        raise Exception(res_json[res_json['e_d']])
    cookies['hello1'] = username
    cookies['hello2'] = 'undefined'
    cookies['hello3'] = ''
    cookies['hello4'] = ''
    cookies['hello5'] = ''
    url_list = ['/portal/page/afterLogin.jsp', '/portal/page/online.jsp',
                '/portal/page/listenClose.jsp',
                '/portal/page/online_heartBeat.jsp',
                '/portal/page/online_showTimer.jsp']
    pl = res_json['portalLink']
    logging.debug('The portal Link is {}'.format(pl))
    afterLogin_params = {
        'v_is_selfLogin': 0,
        'loginType': 3,
        'pl': pl
    }
    online_params = {
        'v_is_selfLogin': 0,
        'loginType': 3,
        'pl': pl
    }
    listenClose_params = {
        'pl': pl
    }
    online_heartBeat_params = {
        'pl': pl
    }
    online_showTimer_params = {
        'v_is_selfLogin': 0,
        'userName': 'null',
        'userPwd': 'null',
        'innerStr': 'null',
        'pl': pl,
        'hlo': 'null',
        'outerStr': 'null',
        'startTime': str(time.time()).replace('.', '')[0:13],
        'loginType': 3
    }
    params_list = [afterLogin_params, online_params, listenClose_params, online_heartBeat_params,
                   online_showTimer_params]
    for item in zip(url_list, params_list):
        logging.info('Get {}'.format(URL + item[0]))
        logging.debug('Parameters: {}'.format(str(item[1])))
        requests.get(URL + item[0], params=item[1], headers=HEADERS, cookies=cookies)
    heartbeat = lambda: do_heartbeat(pl, cookies)
    return heartbeat, logout
