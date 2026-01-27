# AI建模API路由示例
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from catia_mcp_service.di import get_catia_service
from catia_mcp_service.features.ai_suggester import AISuggester
from catia_mcp_service.features.template import TemplateFeature

ai_api = Blueprint('ai_api', __name__)


@ai_api.route('/api/ai/modeling', methods=['POST'])
@jwt_required()
def ai_modeling():
    data = request.get_json()
    desc = data.get('description', '')
    service = get_catia_service()
    suggester = AISuggester(service)
    suggestion = suggester.suggest_modeling(desc)
    if 'template' in suggestion:
        # 自动调用建模模板
        result = TemplateFeature(service).create_flange(suggestion['params'])
        return jsonify({'result': result, 'suggestion': suggestion})
    return jsonify({'error': suggestion.get('error', '未知错误')})


@ai_api.route('/api/ai/knowledge', methods=['POST'])
@jwt_required()
def ai_knowledge():
    data = request.get_json()
    std_type = data.get('type')
    std_id = data.get('id')
    service = get_catia_service()
    suggester = AISuggester(service)
    suggestion = suggester.build_from_knowledge(std_type, std_id)
    if 'template' in suggestion:
        result = TemplateFeature(service).create_flange(suggestion['params'])
        return jsonify({'result': result, 'suggestion': suggestion})
    return jsonify({'error': suggestion.get('error', '未找到标准件')})
