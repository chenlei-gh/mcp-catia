# 三维特征API接口注册
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from catia_mcp_service.di import get_catia_service
from catia_mcp_service.features.feature3d import Feature3D
from catia_mcp_service.api_utils import api_exception_handler, api_logger

feature3d_api = Blueprint('feature3d_api', __name__)


@feature3d_api.route('/api/feature3d/pad', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def pad():
    data = request.get_json()
    sketch_name = data.get('sketch_name')
    length = data.get('length')
    service = get_catia_service()
    result = Feature3D(service).pad(sketch_name, length)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/pocket', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def pocket():
    data = request.get_json()
    sketch_name = data.get('sketch_name')
    length = data.get('length')
    service = get_catia_service()
    result = Feature3D(service).pocket(sketch_name, length)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/shaft', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def shaft():
    data = request.get_json()
    sketch_name = data.get('sketch_name')
    angle = data.get('angle')
    service = get_catia_service()
    result = Feature3D(service).shaft(sketch_name, angle)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/groove', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def groove():
    data = request.get_json()
    sketch_name = data.get('sketch_name')
    angle = data.get('angle')
    service = get_catia_service()
    result = Feature3D(service).groove(sketch_name, angle)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/sweep', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def sweep():
    data = request.get_json()
    profile_sketch = data.get('profile_sketch')
    guide_sketch = data.get('guide_sketch')
    service = get_catia_service()
    result = Feature3D(service).sweep(profile_sketch, guide_sketch)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/loft', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def loft():
    data = request.get_json()
    section_sketches = data.get('section_sketches')
    service = get_catia_service()
    result = Feature3D(service).loft(section_sketches)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/add_body', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def add_body():
    data = request.get_json()
    name = data.get('name')
    service = get_catia_service()
    result = Feature3D(service).add_body(name)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/set_current_body', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def set_current_body():
    data = request.get_json()
    name = data.get('name')
    service = get_catia_service()
    result = Feature3D(service).set_current_body(name)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/boolean', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def boolean_operation():
    data = request.get_json()
    op_type = data.get('op_type')
    body1 = data.get('body1')
    body2 = data.get('body2')
    service = get_catia_service()
    result = Feature3D(service).boolean_operation(op_type, body1, body2)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/hole', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def hole():
    data = request.get_json()
    point_ref = data.get('point_ref')
    depth = data.get('depth')
    service = get_catia_service()
    result = Feature3D(service).hole(point_ref, depth)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/advanced_hole', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def advanced_hole():
    data = request.get_json()
    point_ref = data.get('point_ref')
    depth = data.get('depth')
    diameter = data.get('diameter')
    type_ = data.get('type')
    service = get_catia_service()
    result = Feature3D(service).advanced_hole(point_ref, depth, diameter, type_)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/chamfer', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def chamfer():
    data = request.get_json()
    edge_ref = data.get('edge_ref')
    length = data.get('length')
    angle = data.get('angle')
    service = get_catia_service()
    result = Feature3D(service).chamfer(edge_ref, length, angle)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/advanced_chamfer', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def advanced_chamfer():
    data = request.get_json()
    edge_ref = data.get('edge_ref')
    length = data.get('length')
    angle = data.get('angle')
    mode = data.get('mode')
    service = get_catia_service()
    result = Feature3D(service).advanced_chamfer(edge_ref, length, angle, mode)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/fillet', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def fillet():
    data = request.get_json()
    edge_ref = data.get('edge_ref')
    radius = data.get('radius')
    service = get_catia_service()
    result = Feature3D(service).fillet(edge_ref, radius)
    return jsonify({'result': result})


@feature3d_api.route('/api/feature3d/advanced_fillet', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def advanced_fillet():
    data = request.get_json()
    edge_ref = data.get('edge_ref')
    radius = data.get('radius')
    type_ = data.get('type')
    service = get_catia_service()
    result = Feature3D(service).advanced_fillet(edge_ref, radius, type_)
    return jsonify({'result': result})


# 简要接口文档
"""
三维特征API接口：
- /api/feature3d/pad 拉伸
- /api/feature3d/pocket 切除
- /api/feature3d/shaft 旋转
- /api/feature3d/groove 旋转切除
- /api/feature3d/sweep 扫掠
- /api/feature3d/loft 放样
- /api/feature3d/add_body 新建Body
- /api/feature3d/set_current_body 设为当前Body
- /api/feature3d/boolean 布尔运算
- /api/feature3d/hole 孔
- /api/feature3d/advanced_hole 复杂孔
- /api/feature3d/chamfer 倒角
- /api/feature3d/advanced_chamfer 复杂倒角
- /api/feature3d/fillet 圆角
- /api/feature3d/advanced_fillet 复杂圆角
参数详见各接口JSON体，所有接口需JWT鉴权。
"""
