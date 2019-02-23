from threading import Thread
import requests

class RequestThread(Thread):
    def __init__(self, id, proxies):
        self.id = id
        self.session = requests.session()
        self.session.headers['User-agent'] = 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0'
        if proxies is not None:
            self.session.proxies = proxies        

        super(RequestThread, self).__init__()

    def run(self):
        print('Public Ip - '+self.checkIp())

    def checkIp(self):
        return self.session.get('https://api.ipify.org?format=text').text

