# 权限控制示例（基于角色的API访问）
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from functools import wraps
from flask import jsonify


def role_required(role):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get('role') != role:
                return jsonify({'msg': 'Insufficient permissions'}), 403
            return fn(*args, **kwargs)

        return wrapper

    return decorator
