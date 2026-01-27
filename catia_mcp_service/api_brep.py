# B-Rep/HybridShape/曲面/测量API接口注册
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from catia_mcp_service.di import get_catia_service
from catia_mcp_service.features.param_ops import ParamFeature
from catia_mcp_service.api_utils import api_exception_handler, api_logger

brep_api = Blueprint('brep_api', __name__)


@brep_api.route('/api/brep/get', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def get_brep():
    service = get_catia_service()
    result = ParamFeature(service).get_brep()
    return jsonify({'result': result})


@brep_api.route('/api/brep/measure_body', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def measure_body():
    service = get_catia_service()
    result = ParamFeature(service).measure_body()
    return jsonify({'result': result})


@brep_api.route('/api/brep/measure_face', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def measure_face():
    data = request.get_json()
    face_ref = data.get('face_ref')
    service = get_catia_service()
    result = ParamFeature(service).measure_face(face_ref)
    return jsonify({'result': result})


@brep_api.route('/api/brep/measure_edge', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def measure_edge():
    data = request.get_json()
    edge_ref = data.get('edge_ref')
    service = get_catia_service()
    result = ParamFeature(service).measure_edge(edge_ref)
    return jsonify({'result': result})


# 简要接口文档
"""
B-Rep/HybridShape/曲面/测量API接口：
- /api/brep/get 获取B-Rep
- /api/brep/measure_body 测量体
- /api/brep/measure_face 测量面
- /api/brep/measure_edge 测量边
参数详见各接口JSON体，所有接口需JWT鉴权。
"""
