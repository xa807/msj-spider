from threading import Thread
from queue import Queue

import time
from lxml import etree
from common import log
from common import ua

import requests

class MsjSpider(Thread):

    def __init__(self, q: Queue, itemQueue: Queue):
        super().__init__()
        self.queue = q
        self.filter_urls = []  # 用于去重
        self.itemQueue = itemQueue

    def download(self, url):
        resp = requests.get(url, headers={
                    'User-Agent': ua.get_ua()
                })
        if resp.status_code == 200:
            log.info('GET %s 200 OK' %url)
            self.parse(resp.text)
        else:
            log.error('Error %s %s ' %(url, resp.status_code))


    def parse(self, html):
        root = etree.HTML(html)
        # 获取当前页面的数据
        a_list = root.xpath('//div[@id="listtyle1_list"]//a')

        for a in a_list:
            info = {}
            info['name'] = a.xpath('./@title')[0]
            info['author'] = a.xpath('.//div[@class="c1"]/em/text()')[0]
            step = a.xpath('.//li[@class="li1"]/text()')[0]
            info['steps'], info['steps_time'] = step.split('/')

            practice = a.xpath('.//li[@class="li2"]/text()')[0]
            info['practice'], info['taste'] = practice.split('/')

            info['image'] = a.xpath('./img/@src')[0]

            log.debug(info)
            self.itemQueue.put(info)

        relation_urls = root.xpath('//dl[starts-with(@class, "listnav_dl_style1")]//a/@href')
        next_page_url_a = root.xpath('//div[@class="listtyle1_page_w"]/a[last()]')
        if next_page_url_a:
            next_page_url= next_page_url_a[0].xpath('./@href')[0]
            relation_urls.insert(0, next_page_url)

        for url in relation_urls:
            if url not in self.filter_urls:
                self.queue.put(url)
                self.filter_urls.append(url)
                time.sleep(1)

    def run(self):
        while True:
            try:
                url = self.queue.get(timeout=60)
                log.info('downloading %s' % url)
                self.download(url)
            except Exception as e:
                log.error(e)
                break

