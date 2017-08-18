# -*-coding:utf-8 -*-

from db_basic import engine
from sqlalchemy.orm import *
from db.table import *
from decorators.decorator import db_save_decorator

@db_save_decorator
def save_style(styles):
	conn=engine.connect()
	data=style.insert()
	conn.execute(data,styles)

@db_save_decorator
def save_playlist(playlists):
	conn=engine.connect()
	data=playlist.insert()
	conn.execute(data,playlists)

@db_save_decorator
def save_song(songs):
	conn=engine.connect()
	data=song.insert()
	conn.execute(data,songs)

@db_save_decorator
def save_comment(comments):
	conn=engine.connect()
	data=comment.insert()
	conn.execute(data,comments)

@db_save_decorator
def save_user_info(info):
	conn=engine.connect()
	data=user.insert()
	conn.execute(data,info)


