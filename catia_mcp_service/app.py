from catia_mcp_service.api_brep import brep_api
from catia_mcp_service.api_assembly import assembly_api

# 主程序入口，统一调用各功能模块
from flask import Flask, request, jsonify
from flask_restful import Resource
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required
from catia_mcp_service.service import CATIAService
from catia_mcp_service.features.sketch import SketchFeature

from catia_mcp_service.api_sketch import sketch_api
from catia_mcp_service.api_feature3d import feature3d_api
from catia_mcp_service.api_param import param_api

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
jwt = JWTManager(app)

# 注册Blueprint
# 注册Blueprint
app.register_blueprint(sketch_api)
app.register_blueprint(feature3d_api)
app.register_blueprint(param_api)
app.register_blueprint(assembly_api)
app.register_blueprint(brep_api)


# 示例：草图API
class CreateSketch(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        plane = data.get('plane')
        service = CATIAService()
        service.connect()
        result = SketchFeature(service).create_sketch(plane)
        return jsonify({'result': result})


# 其他API同理，调用对应Feature
# ...（此处可继续添加其他API资源类，调用各自Feature）...


if __name__ == '__main__':
    app.run(debug=True)
