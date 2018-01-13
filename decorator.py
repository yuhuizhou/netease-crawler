# -*-coding:utf-8 -*-
from functools import wraps
from traceback import format_tb

from logger.log import parser, crawler, storage



# timeout decorator
def timeout_decorator(func):
    @wraps(func)
    def time_limit(*args, **kargs):
        try:
            return func(*args, **kargs)
        except Exception as e:
            crawler.error('failed to crawl {url}，here are details:{e}'.format(url=args[0], e=e))
            return ''

    return time_limit


def db_save_decorator(func):
    @wraps(func)
    def save(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            storage.error('db operation error，here are details{}'.format(e))
            #storage.warning('transaction rollbacks')
            #db_session.rollback()
    return save


def parse_decorator(return_value):
    """
    :param return_value: catch exceptions when parsing pages, return the default value
    :return: the default value is 0,'',[],False,{} or None
    """
    def page_parse(func):
        @wraps(func)
        def handle_error(*keys):
            try:
                return func(*keys)
            except Exception as e:
                parser.error(e)
                return return_value
        return handle_error
    return page_parse


