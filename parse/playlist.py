# -*- coding:utf8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import re
import requests
reload(sys)
sys.setdefaultencoding('utf-8')


def get_playlist(url):
    detail=[]
    driver = webdriver.Chrome()
    driver.get(url)
    driver.switch_to.frame(driver.find_element_by_name('contentFrame'))
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, 'lxml')
    list = soup.find('ul',{'class':'m-cvrlst f-cb'}).find_all('li')
    for li in list:
        href = 'http://music.163.com/#'+li.find('a',{'class': 'msk'})['href']
        title=li.find('a',{'class': 'msk'})['title']
        dict={'pname':title,'plink':href,'crawled':0}
        detail.append(dict)
    return detail

def get_song(p_link):
    driver = webdriver.Chrome()
    driver.get(p_link)
    driver.switch_to.frame(driver.find_element_by_name('contentFrame'))
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, 'lxml')
    spans= soup.find_all('span', {'class': 'txt'})
    arts=soup.find('tbody').find_all('a',{'hidefocus':'true'})
    albums=soup.find('tbody').find_all('tr')
    detail=[]
    url='http://music.163.com/weapi/v1/resource/comments/R_SO_4_'
    for (span,art,album) in zip(spans,arts,albums):
        l = span.find('a')['href']
        href =url+l[9:]+'?csrf_token='
        title = span.find('b')['title']
        singer=art.get_text()
        singer_link='http://music.163.com/#'+art['href']
        aname=album.find_all('td')[4].find('a')['title']
        alink=album.find_all('td')[4].find('a')['href']
        dict={'sname':title,'singer':singer,'song_link':href,'singer_link':singer_link,'aname':aname,'album_link':alink}
        detail.append(dict)
    return detail
 
if __name__ == '__main__':
    p_link='http://music.163.com/#/playlist?id=865078530'
    get_song(p_link)
    
