# -*-coding:utf-8 -*-

from tasks import user
from tasks import comment
from db.save import save_style
from db.table import engine,metadata
from parse.playlist import get_style,get_max_page


if __name__ == '__main__':

	metadata.create_all(engine)    ##create tables for storage
	#metadata.drop_all(engine)     ##drop tables

 	base_url = 'http://music.163.com/discover/playlist/'  
	style_links=get_style(base_url)    
	save_style(style_links)
	user.execute_user_task()  ##start to crawl user information
	comment.execute_playlist_task()   #start to crawl comments 
