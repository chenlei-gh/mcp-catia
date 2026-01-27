# 服务工厂与依赖注入
from catia_mcp_service.service import CATIAService


def get_catia_service():
    service = CATIAService()
    service.connect()
    return service
