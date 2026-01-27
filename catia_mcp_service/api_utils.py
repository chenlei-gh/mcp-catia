# 统一异常处理与日志装饰器
import logging
from functools import wraps
from flask import jsonify


def api_exception_handler(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            logging.exception(f"API异常: {e}")
            return jsonify({'error': str(e)}), 500

    return wrapper


def api_logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        logging.info(f"调用API: {fn.__name__}")
        return fn(*args, **kwargs)

    return wrapper
