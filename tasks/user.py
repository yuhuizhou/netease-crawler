# coding:utf-8

from __future__ import absolute_import
from tasks.celery import app
from parse.user import get_user_info
from db.save import save_user_info
from db.search import get_user_link

@app.task(ignore_result=True)
def crawl_user_information(ulink):
    info=get_user_info(ulink)
    save_user_info(info)
    
@app.task(ignore_result=True)
def execute_user_task():
    ulinks=get_user_link()
    for ulink in ulinks[0:10]:
        app.send_task('tasks.user.crawl_user_information', args=(ulink[0],), queue='user_crawler', routing_key='user_info')
