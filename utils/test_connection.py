import requests


def test_connection():
    url = r'http://http204.sinaapp.com/generate_204'
    try:
        r = requests.get(url)
        if r.status_code == 204:
            return True
        else:
            return False
    except (ConnectionError, requests.exceptions.Timeout) as e:
        return False
