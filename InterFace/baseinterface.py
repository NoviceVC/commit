import requests,pytest
from Include.commit.Base.helper import Configparser

class BaseInterface(object):
    _requests_url = '/admin'
    def __init__(self):
        self.base_url = ''.join(Configparser.config('crm','url')+self._requests_url)
        self.session = requests.Session()

if __name__ == '__main__':
    BaseInterface()