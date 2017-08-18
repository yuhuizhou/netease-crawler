# -*- coding:utf8 -*-

import time
import requests
from headers import headers
from bs4 import BeautifulSoup
from logger.log import crawler
from decorators.decorator import parse_decorator,timeout_decorator



@parse_decorator('')
@timeout_decorator
def get_soup(url):

    crawler.info('the crawling url is {url}'.format(url=url))
    html=requests.get(url,headers=headers).text
    time.sleep(5)
    soup = BeautifulSoup(html, 'lxml')
    return soup