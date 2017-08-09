# -*-coding:utf-8 -*-
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connect_string='mysql+mysqldb://root:password@localhost:3306/netease?charset=utf8mb4'
engine=create_engine(connect_string,echo=True) #创建连接引擎
Base=declarative_base()  #d定义基类
Session=sessionmaker(bind=engine)
db_session=Session()
metadata=MetaData(engine) #通过连接引擎抓取元数据（元数据：描述数据的数据）


__all__ = ['engine', 'Base', 'db_session', 'metadata']



