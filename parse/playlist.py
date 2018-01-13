# -*- coding:utf8 -*-

import sys
import json
from bs4 import BeautifulSoup
from parse.page import get_soup
from decorator import parse_decorator
reload(sys)
sys.setdefaultencoding('utf-8')

@parse_decorator(0)
def get_max_page(style_link):
    soup=get_soup(style_link)
    max_page=soup.find('span',{'class':'zdot'}).find_next_sibling('a',{'class':'zpgi'}).string
    return max_page

@parse_decorator([])
def get_style(basic_url):
    detail=[]
    soup = get_soup(basic_url)
    dls=soup.find_all('dl',{'class':'f-cb'})
    for dl in dls:
        alists=dl.find('dd').find_all('a',{'class':'s-fc1'})
        for a in alists:
            link='http://music.163.com'+a['href']
            max_page=get_max_page(link)
            dict={'name':a['data-cat'],'link':link,'max_page':max_page}
            detail.append(dict)
    return detail

@parse_decorator([])
def get_playlist(url):
    detail=[]
    soup = get_soup(url)
    lis= soup.find('ul',{'class':'m-cvrlst f-cb'}).find_all('li')
    for li in lis:
        href = 'http://music.163.com'+li.find('a',{'class': 'msk'})['href']
        title=li.find('a',{'class': 'msk'})['title']
        playcount=li.find('span',{'class':'nb'}).string
        dict={'pname':title,'plink':href,'playcount':playcount,'crawled':0}
        detail.append(dict)
    return detail

@parse_decorator([])
def get_song(p_link):
    soup = soup = get_soup(p_link)
    string=soup.find('textarea').string
    json_dict=json.loads(string)
    detail=[]
    for dict in json_dict:
        basic_url='http://music.163.com/weapi/v1/resource/comments/'
        href =basic_url+dict['commentThreadId']+'?csrf_token='
        name = dict['name']
        singer=dict['artists'][0]['name']
        singer_link='http://music.163.com/#/artist?id='+str(dict['artists'][0]['id'])
        aname=dict['album']['name']
        alink='http://music.163.com/#/album?id='+str(dict['album']['id'])
        dict={'sname':name,'singer':singer,'song_link':href,'singer_link':singer_link,'aname':aname,'album_link':alink}
        detail.append(dict)
    return detail


    
