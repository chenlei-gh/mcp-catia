# OpenAPI/Swagger自动生成（Flask-RESTX示例）
from flask_restx import Api


def register_api(app):
    api = Api(app, version='1.0', title='CATIA MCP API', description='CATIA自动化REST接口文档')
    # 可在此注册各命名空间
    # from .api_sketch import sketch_api
    # api.add_namespace(sketch_api, path='/api/sketch')
    return api
