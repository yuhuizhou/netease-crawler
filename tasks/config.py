# -*- coding:utf-8 -*-
 
from __future__ import absolute_import
from kombu import Exchange, Queue
from datetime import timedelta

CELERY_TIMEZONE='Asia/Shanghai'
CELERY_ENABLE_UTC=True
CELERY_ACCEPT_CONTENT=['json']
CELERY_TASK_SERIALIZER='json'
CELERY_RESULT_SERIALIZER='json'
CELERYBEAT_SCHEDULE={
    'comment_task': {
        'task': 'tasks.comment.excute_comment_task',
        'schedule': timedelta(seconds=5),
        'options': {'queue': 'comment_crawler', 'routing_key': 'comment_info'}
    },
    'playlist_task': {
        'task': 'tasks.workers.execute_playlist_task',
        'schedule': timedelta(seconds=5),
        'options': {'queue': 'playlist_crawler', 'routing_key': 'playlist_info'}
    },

}

CELERY_QUEUES=(
    Queue('playlist_crawler', exchange=Exchange('playlist_crawler', type='direct'),routing_key='playlist_info'),
    Queue('comment_crawler', exchange=Exchange('comment_crawler', type='direct'),routing_key='comment_info'),
    Queue('song_crawler', exchange=Exchange('song_crawler', type='direct'),routing_key='song_info'),
    Queue('user_crawler', exchange=Exchange('user_crawler', type='direct'),routing_key='user_info'),
)
