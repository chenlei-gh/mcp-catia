# API分层示例：业务逻辑与API分离
# 业务逻辑层（service/feature已实现）
# 这里只示例API层如何调用业务层
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from catia_mcp_service.di import get_catia_service
from catia_mcp_service.features.sketch import SketchFeature
from catia_mcp_service.api_utils import api_exception_handler, api_logger

sketch_api = Blueprint('sketch_api', __name__)


@sketch_api.route('/api/sketch/create', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def create_sketch():
    data = request.get_json()
    plane = data.get('plane')
    service = get_catia_service()
    result = SketchFeature(service).create_sketch(plane)
    return jsonify({'result': result})


# 多段线
@sketch_api.route('/api/sketch/polyline', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def draw_polyline():
    data = request.get_json()
    sketch_name = data.get('sketch_name')
    points = data.get('points')  # [[x1, y1], [x2, y2], ...]
    service = get_catia_service()
    result = SketchFeature(service).draw_polyline(sketch_name, points)
    return jsonify({'result': result})


# 样条
@sketch_api.route('/api/sketch/spline', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def draw_spline():
    data = request.get_json()
    sketch_name = data.get('sketch_name')
    points = data.get('points')
    service = get_catia_service()
    result = SketchFeature(service).draw_spline(sketch_name, points)
    return jsonify({'result': result})


# 镜像
@sketch_api.route('/api/sketch/mirror', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def mirror_elements():
    data = request.get_json()
    sketch_name = data.get('sketch_name')
    element_indices = data.get('element_indices')
    axis_index = data.get('axis_index')
    service = get_catia_service()
    result = SketchFeature(service).mirror_elements(sketch_name, element_indices, axis_index)
    return jsonify({'result': result})


# 阵列
@sketch_api.route('/api/sketch/array', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def array_elements():
    data = request.get_json()
    sketch_name = data.get('sketch_name')
    element_indices = data.get('element_indices')
    count = data.get('count')
    dx = data.get('dx')
    dy = data.get('dy')
    service = get_catia_service()
    result = SketchFeature(service).array_elements(sketch_name, element_indices, count, dx, dy)
    return jsonify({'result': result})


# 批量约束
@sketch_api.route('/api/sketch/constraints/batch', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def add_constraints_batch():
    data = request.get_json()
    sketch_name = data.get('sketch_name')
    constraints = data.get('constraints')  # [(type, args), ...]
    service = get_catia_service()
    result = SketchFeature(service).add_constraints_batch(sketch_name, constraints)
    return jsonify({'result': result})


# 分组
@sketch_api.route('/api/sketch/group', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def group_elements():
    data = request.get_json()
    sketch_name = data.get('sketch_name')
    element_indices = data.get('element_indices')
    service = get_catia_service()
    result = SketchFeature(service).group_elements(sketch_name, element_indices)
    return jsonify({'result': result})


# 投影
@sketch_api.route('/api/sketch/project', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def project_geometry():
    data = request.get_json()
    sketch_name = data.get('sketch_name')
    target_name = data.get('target_name')
    service = get_catia_service()
    result = SketchFeature(service).project_geometry(sketch_name, target_name)
    return jsonify({'result': result})


# 元素属性
@sketch_api.route('/api/sketch/element/property', methods=['POST'])
@jwt_required()
@api_exception_handler
@api_logger
def set_element_property():
    data = request.get_json()
    sketch_name = data.get('sketch_name')
    element_index = data.get('element_index')
    color = data.get('color')
    linetype = data.get('linetype')
    layer = data.get('layer')
    service = get_catia_service()
    result = SketchFeature(service).set_element_property(sketch_name, element_index, color, linetype, layer)
    return jsonify({'result': result})


# 文档说明（简要）
"""
草图与几何API接口：
- /api/sketch/create 新建草图
- /api/sketch/polyline 多段线
- /api/sketch/spline 样条
- /api/sketch/mirror 镜像
- /api/sketch/array 阵列
- /api/sketch/constraints/batch 批量约束
- /api/sketch/group 分组
- /api/sketch/project 投影
- /api/sketch/element/property 元素属性
参数详见各接口JSON体，所有接口需JWT鉴权。
"""
