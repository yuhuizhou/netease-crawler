# -*- coding:utf8 -*-

import sys
from bs4 import BeautifulSoup
from parse.page import get_soup
from decorators.decorator import parse_decorator
reload(sys)
sys.setdefaultencoding('utf-8')


@parse_decorator([])
def get_user_info(ulink):
	soup=get_soup(ulink)
	introduce=soup.find('div',{'class':'inf s-fc3 f-brk'}).string
	div=soup.find('div',{'class':'inf s-fc3'}).find('span')
	location=div.string
	age=div.find_next_sibling('span').string
	event_link=soup.find('li',{'class':'fst'}).find('a')['href']
	li=soup.find('li',{'class':'fst'}).find_next_sibling('li')
	follow_link=li.find('a')['href']
	fan_link=li.find_next_sibling('li').find('a')['href']
	follow_count=int(soup.find('strong',{'id':'follow_count'}).string)
	fan_count=int(soup.find('strong',{'id':'fan_count'}).string)
	rank_num=soup.find('div',{'id':'rHeader'}).find('h4').string[4:][:-1]
	rank_link=soup.find('a',{'id':'more'})['href']
	dict={'user_link':ulink,'introduce':introduce,'location':location,'age':age,'event_link':event_link,'follow_link':follow_link,'fan_link':fan_link,'follow_count':follow_count,'fan_count':fan_count,'rank_num':rank_num,'rank_link':rank_link}
	return dict



	