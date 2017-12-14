import requests


def test_connection():
    """
    test internet connection via http://http204.sinaapp.com/generate_204
    :return: True if success else False
    """
    url = r'http://http204.sinaapp.com/generate_204'
    try:
        r = requests.get(url)
        if r.status_code == 204:
            return True
        else:
            return False
    except:
        return False
