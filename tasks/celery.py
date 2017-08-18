# coding:utf-8

from __future__ import absolute_import
from celery import Celery


app = Celery('tasks', include=['tasks.comment','tasks.user'], broker='redis://localhost:6379/1', backend='redis://localhost:6379/2')

app.config_from_object('tasks.config')

if __name__ == '__main__':
    app.start()