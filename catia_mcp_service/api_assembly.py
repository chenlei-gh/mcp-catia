# 装配API接口注册
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from catia_mcp_service.di import get_catia_service
from catia_mcp_service.features.assembly import AssemblyFeature
from catia_mcp_service.api_utils import api_exception_handler, api_logger

assembly_api = Blueprint('assembly_api', __name__)


@assembly_api.route('/api/assembly/create_product', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def create_product():
    data = request.get_json()
    name = data.get('name')
    service = get_catia_service()
    result = AssemblyFeature(service).create_product(name)
    return jsonify({'result': result})


@assembly_api.route('/api/assembly/add_part', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def add_part():
    data = request.get_json()
    part_path = data.get('part_path')
    service = get_catia_service()
    result = AssemblyFeature(service).add_part(part_path)
    return jsonify({'result': result})


@assembly_api.route('/api/assembly/remove_part', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def remove_part():
    data = request.get_json()
    index = data.get('index')
    service = get_catia_service()
    result = AssemblyFeature(service).remove_part(index)
    return jsonify({'result': result})


@assembly_api.route('/api/assembly/add_constraint', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def add_constraint():
    data = request.get_json()
    type_ = data.get('type')
    ref1 = data.get('ref1')
    ref2 = data.get('ref2')
    service = get_catia_service()
    result = AssemblyFeature(service).add_constraint(type_, ref1, ref2)
    return jsonify({'result': result})


# 简要接口文档
"""
装配API接口：
- /api/assembly/create_product 新建装配
- /api/assembly/add_part 添加零部件
- /api/assembly/remove_part 移除零部件
- /api/assembly/add_constraint 添加装配约束
参数详见各接口JSON体，所有接口需JWT鉴权。
"""
