# -*-coding:utf-8 -*-

from __future__ import absolute_import
from tasks.celery import app
from parse.comment import get_comment
from db.search import get_style_link,get_max_num
from db.save import save_playlist,save_song,save_comment
from parse.playlist import get_playlist,get_song,get_max_page

@app.task(ignore_result=True)
def crawl_comment_by_song(slink):
   comments=get_comment(slink)
   save_comment(comments)

@app.task(ignore_result=True)
def crawl_song_by_playlist(plink):
	songs=get_song(plink)
	save_song(songs)
	for song in songs[0:1]:
		app.send_task('tasks.comment.crawl_comment_by_song', args=(song['song_link'],), queue='comment_crawler', routing_key='comment_info')
		
@app.task(ignore_result=True)
def crawl_playlist_by_page(link,page_num):
    offset= (page_num)*35
    cur_url = link+'&limit=35&offset={}'.format(offset)
    playlists= get_playlist(cur_url)
    save_playlist(playlists)
    for playlist in playlists[0:1]:
    	app.send_task('tasks.comment.crawl_song_by_playlist', args=(playlist['plink'],), queue='song_crawler', routing_key='song_info')

@app.task(ignore_result=True)
def execute_playlist_task():
	style_links=get_style_link()
	for link in style_links[0:1]:
		max_page=get_max_num(link[0])
		for page_num in range(0,max_page+1):
			app.send_task('tasks.comment.crawl_playlist_by_page', args=(link[0],page_num,), queue='playlist_crawler', routing_key='playlist_info')


