# -*- coding:utf8 -*-

from bs4 import BeautifulSoup
import sys
import json
import requests
from save import save_style
from search import get_style_link,get_max_num
from table import metadata,engine
reload(sys)
sys.setdefaultencoding('utf-8')

def get_max_page(style_link):
    html=requests.get(style_link).text
    soup = BeautifulSoup(html, 'lxml')
    max_page=soup.find('span',{'class':'zdot'}).find_next_sibling('a',{'class':'zpgi'}).string
    return max_page



def get_style(basic_url):
    html=requests.get(basic_url).text
    detail=[]
    soup = BeautifulSoup(html, 'lxml')
    dls=soup.find_all('dl',{'class':'f-cb'})
    for dl in dls:
        alists=dl.find('dd').find_all('a',{'class':'s-fc1'})
        for a in alists:
            link='http://music.163.com'+a['href']
            max_page=get_max_page(link)
            dict={'name':a['data-cat'],'link':link,'max_page':max_page}
            detail.append(dict)
    return detail


def get_playlist(url):
    html=requests.get(url).text
    detail=[]
    soup = BeautifulSoup(html, 'lxml')
    lis= soup.find('ul',{'class':'m-cvrlst f-cb'}).find_all('li')
    for li in lis:
        href = 'http://music.163.com'+li.find('a',{'class': 'msk'})['href']
        title=li.find('a',{'class': 'msk'})['title']
        playcount=li.find('span',{'class':'nb'}).string
        dict={'pname':title,'plink':href,'playcount':playcount,'crawled':0}
        detail.append(dict)
    return detail


def get_song(p_link):
    html=requests.get(p_link).content
    soup = BeautifulSoup(html, 'lxml')
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

if __name__ == '__main__':
    #metadata.drop_all(engine)
    #headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'}
    #basic_url='http://music.163.com/discover/playlist/'
    #detail=get_style(basic_url)
    #print detail
    #save_style(detail)
    links=get_style_link()
    for link in links[0:10]:
       print link[0]
       num=get_max_num(link[0])
       print num[0]
       print type(num[0])
       #num[0]=str(num[0])
       #num=num[0].encode('utf-8')
       #num=int(num)
       #print type(num)
       #print type('fajkasdf{}'.format(num*35))
    #get_playlist(basic_url)
    
