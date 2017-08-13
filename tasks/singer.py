# coding:utf-8

from __future__ import absolute_import
from tasks.celery import app
from parse.playlist import get_album,get_song
from db.save import save_album,save_song


base_url = 'http://music.163.com/#/discover/playlist/?order=hot&cat={}&limit=35&offset={}'
titles=['%E5%8D%8E%E8%AF%AD','%E6%AC%A7%E7%BE%8E&']

@app.task(ignore_result=True)
def crawl_link_by_playlist(p_link):
	songs=get_song(p_link)
	save_song(songs)

@app.task(ignore_result=True)
def crawl_playlist_by_page(title,page_num):
    cur_num= (page_num)*35
    cur_url = base_url.format(title,cur_num)
    albums= get_album(cur_url)
    save_album(albums)
    for album in albums[0:1]:
    	app.send_task('tasks.workers.crawl_link_by_playlist', args=(album['alink'],), queue='link_crawler', routing_key='link_info')

@app.task(ignore_result=True)
def execute_singer_task():
    for title in titles:
    	for page_num in range(0,2):
            app.send_task('tasks.workers.crawl_playlist_by_page', args=(title,page_num,), queue='playlist_crawler', routing_key='playlist_info')
