# -*-coding:utf-8 -*-
from db.save import save_style
from parse.playlist import get_style

base_url = 'http://music.163.com/discover/playlist/'
results=get_style(base_url)
save_style(results)