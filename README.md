# NeteaseCrawler
a distributed crawler base on celery


#依赖版本 具体见requirements.txt

MySQL 5.7
Python 2.7
celery==3.1.25
redis==2.10.5


## 启动celery 
celery -A tasks worker --loglevel=info

##启动 redis
redis-server

##开始任务

Python start.py



