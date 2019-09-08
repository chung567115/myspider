import time
import requests
from bs4 import BeautifulSoup


class ProxyIp:
    
    def __init__(self, page=1000):
        self.proxies = []
        self.verify_pro = []
        self.page = page
        self.headers = {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        self.get_proxies()
    
    def get_proxies(self):
        page = 0
        while page < self.page:
            page += 1
            # url = 'https://www.kuaidaili.com/free/inha/%d' % page
            url = 'http://www.qydaili.com/free/?action=china&page=%d' % page
            try:
                html = requests.get(url, headers=self.headers).content
                soup = BeautifulSoup(html, 'lxml')
                # time.sleep(1)
                trs = soup.find(id='content').find(name='tbody').find_all(name='tr')
                for tr in trs:
                    tds = tr.find_all(name='td')
                    protocol = tds[3].get_text().lower()
                    if protocol == 'http' or tds[0].get_text() == '' or tds[1].get_text() == '':
                        continue
                    self.proxies.append(tds[0].get_text() + ':' + tds[1].get_text())
            except Exception as e:
                print(e)
                pass


if __name__ == '__main__':
    a = ProxyIp()
    with open('qydaili_proxies.txt', 'w+') as f:
        for proxy in a.proxies:
            f.write(proxy + '\n')
