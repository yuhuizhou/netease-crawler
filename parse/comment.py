# -*- coding:utf8 -*-

import requests
import json
from parse.params import get_params
from decorator import parse_decorator

@parse_decorator([])
def get_comment(slink):
	detail=[]
	data = get_params()
	json_dict = json.loads(requests.post(slink, data=data).content)
	hot_comments = json_dict['hotComments']
	for item in hot_comments:
		comment = item['content']  # 评论内容
		likecount = int(item['likedCount'])  # 点赞总数
		nickname = item['user']['nickname']  # 昵称
		user_link='http://music.163.com/user/home?id='+str(item['user']['userId'])
		dict={'nickname':nickname,'likecount':likecount,'detail':comment,'user_link':user_link,'song_link':slink}
		detail.append(dict)
	return detail
