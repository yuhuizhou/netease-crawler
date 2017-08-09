# coding:utf-8

from __future__ import absolute_import
from tasks.celery import app
from db.save import save_comment
from parse.comment import get_comment
from db.save import save_playlist,save_song
from parse.playlist import get_playlist,get_song


base_url = 'http://music.163.com/#/discover/playlist/?order=hot&cat={}&limit=35&offset={}'
titles=['%E5%8D%8E%E8%AF%AD','%E6%AC%A7%E7%BE%8E&']


@app.task(ignore_result=True)
def crawl_comment_by_song(slink):
   comments=get_comment(slink)
   save_comment(comments)

@app.task(ignore_result=True)
def crawl_song_by_playlist(p_link):
	songs=get_song(p_link)
	save_song(songs)
	for song in songs[0:10]:
		app.send_task('tasks.comment.crawl_comment_by_song', args=(song['song_link'],), queue='comment_crawler', routing_key='comment_info')
		
@app.task(ignore_result=True)
def crawl_playlist_by_page(title,page_num):
    cur_num= (page_num)*35
    cur_url = base_url.format(title,cur_num)
    playlists= get_playlist(cur_url)
    save_playlist(playlists)
    for playlist in playlists[0:1]:
    	app.send_task('tasks.comment.crawl_song_by_playlist', args=(playlist['plink'],), queue='song_crawler', routing_key='song_info')

@app.task(ignore_result=True)
def execute_playlist_task():
    for title in titles:
    	for page_num in range(0,2):
            app.send_task('tasks.comment.crawl_playlist_by_page', args=(title,page_num,), queue='playlist_crawler', routing_key='playlist_info')


