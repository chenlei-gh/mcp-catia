# 参数/表达式/设计表API接口注册
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from catia_mcp_service.di import get_catia_service
from catia_mcp_service.features.param_ops import ParamFeature
from catia_mcp_service.api_utils import api_exception_handler, api_logger

param_api = Blueprint('param_api', __name__)


@param_api.route('/api/param/set', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def set_parameter():
    data = request.get_json()
    name = data.get('name')
    value = data.get('value')
    service = get_catia_service()
    result = ParamFeature(service).set_parameter(name, value)
    return jsonify({'result': result})


@param_api.route('/api/param/get', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def get_parameter():
    data = request.get_json()
    name = data.get('name')
    service = get_catia_service()
    result = ParamFeature(service).get_parameter(name)
    return jsonify({'result': result})


@param_api.route('/api/param/link', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def link_parameter():
    data = request.get_json()
    target = data.get('target')
    source = data.get('source')
    service = get_catia_service()
    result = ParamFeature(service).link_parameter(target, source)
    return jsonify({'result': result})


@param_api.route('/api/param/part_property/get', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def get_part_property():
    data = request.get_json()
    prop = data.get('prop')
    service = get_catia_service()
    result = ParamFeature(service).get_part_property(prop)
    return jsonify({'result': result})


@param_api.route('/api/param/part_property/set', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def set_part_property():
    data = request.get_json()
    prop = data.get('prop')
    value = data.get('value')
    service = get_catia_service()
    result = ParamFeature(service).set_part_property(prop, value)
    return jsonify({'result': result})


# 简要接口文档
"""
参数/表达式/设计表API接口：
- /api/param/set 设置参数
- /api/param/get 获取参数
- /api/param/link 参数关联
- /api/param/part_property/get 获取零件属性
- /api/param/part_property/set 设置零件属性
参数详见各接口JSON体，所有接口需JWT鉴权。
"""
