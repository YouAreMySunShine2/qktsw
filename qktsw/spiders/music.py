# -*- coding: utf-8 -*-
import scrapy

from qktsw.items import QktswItem


class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['*']
    urls = []
    for i in range(0, 100):
        url = "http://www.qktsw.com/downm.asp?id=51855&t=0&k=" + '%d' % i + '#'
        urls.append(url)
    start_urls = urls

    def parse(self, response):
        url = response._url.split("=")
        sub = QktswItem()
        sub["fileName"] = url[len(url)-1] + ".mp3"
        sub["url"] = response.css("a::attr(thunderhref)").extract()[0]
        yield sub
