__author__ = 'dzp'
from imp import reload
from scrapy.http import Request,FormRequest
from scrapy.spider import Spider
from scrapy.selector import Selector
from youtube.items import YoutubeItem
from youtube.settings import *

class youtubeSpider(Spider):
    name = "youtube"
    allowed_domains=["https://www.youtube.com/feed/trending"]
    start_urls=['https://www.youtube.com/feed/trending']

    def __init__(self):
        self.headers =HEADER
        self.cookies=COOKIES

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield FormRequest(url, meta = {'cookiejar': i}, \
                              headers = self.headers, \
                              cookies =self.cookies,
                              callback = self.parse)#jump to login page


    def parse(self,response):
        #sel是页面源代码，载入scrapy.selector
        urls=[]
        sel = Selector(response)
        print(sel.xpath('//*[@id="item-section-931744"]').extract())