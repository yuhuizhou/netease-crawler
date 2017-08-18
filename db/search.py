# -*-coding:utf-8 -*-
from sqlalchemy import text
from db_basic import db_session
from db.table import *
from db.model import *


def get_style_link():
	return db_session.query(Style.link).all()

def get_max_num(link):
	max_num=db_session.query(Style.max_page).filter(Style.link==link).first()
	return int((max_num)[0].encode('utf-8'))

def get_user_link():
	return db_session.query(Comment.user_link).all()



'''def get_playlist_link():
	return db_session.query(Playlist.plink).all()

def judge_crawl(alink):
	result=db_session.query(Album.crawled).filter(Album.alink==alink).first()
	print result[0]
	if result[0]==0:
		return True
	else:
		return False

def update_alink(alink):
	db_session.query(Album.alink).filter(Album.alink==alink).update({Album.crawled:1})
	db_session.commit()'''

if __name__ == '__main__':
	alink='http://music.163.com/#/playlist?id=870142039'
	results=get_song_link(alink)
	for result in results:
		print result[0]

	