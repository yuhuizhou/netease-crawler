# -*-coding:utf-8 -*-
#from db.db_basic import db_session
from db_basic import engine
from sqlalchemy.orm import *
from table import *

def save_style(styles):
	conn=engine.connect()
	data=style.insert()
	result=conn.execute(data,styles)

def save_playlist(playlists):
	conn=engine.connect()
	data=playlist.insert()
	result=conn.execute(data,playlists)
	
def save_song(songs):
	conn=engine.connect()
	data=song.insert()
	result=conn.execute(data,songs)

def save_comment(comments):
	conn=engine.connect()
	data=comment.insert()
	result=conn.execute(data,comments)

#def save_user_info(info):

