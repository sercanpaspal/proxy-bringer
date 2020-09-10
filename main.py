import requests
from time import sleep
from bs4 import BeautifulSoup
from threading import Thread


class ProxyBringer:
    debug = False
    check_interval = 60
    used_proxies = []
    proxies = []
    proxy_urls = [
        "https://www.sslproxies.org",
        "https://www.socks-proxy.net",
        "https://free-proxy-list.net/uk-proxy.html",
        "https://free-proxy-list.net/anonymous-proxy.html",
        "https://us-proxy.org",
        "https://free-proxy-list.net",
    ]

    def __init__(self, debug=False, check_interval=60):
        self.debug = debug
        self.check_interval = check_interval

    def log(self, string):
        if self.debug:
            print(string)

    def get_proxies_from_url(self, source):
        response = requests.get(source)
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find(class_='table table-striped table-bordered').findAll('tr')
        for row in rows:
            cols = row.findAll('td')
            if len(cols) > 1:
                proxy = cols[0].text + ':' + cols[1].text
                if proxy not in self.proxies and proxy not in self.used_proxies:
                    self.proxies.append(proxy)

    def get_proxy(self):
        if len(self.proxies) > 0:
            proxy = self.proxies.pop(0)
            self.log(proxy + " Proxy Getting...")
            self.used_proxies.append(proxy)
            return proxy
        else:
            return None

    def check_all_proxy_urls(self):
        self.log("Checking all proxy sources..")
        while True:
            for url in self.proxy_urls:
                try:
                    self.get_proxies_from_url(url)
                except:
                    self.log(url + " Checking Error!")
                self.log(url + " Checked!")
            sleep(self.check_interval)

    def start(self):
        self.log("Starting proxy service..")
        Thread(target=self.check_all_proxy_urls).start()
