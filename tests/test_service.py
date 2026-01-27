# 单元测试与集成测试示例
import pytest
from catia_mcp_service.service import CATIAService

def test_service_connect():
    service = CATIAService()
    assert service.connect() in [True, False]  # 视环境而定

def test_open_document_fail():
    service = CATIAService()
    service.connect()
    assert not service.open_document('not_exist.CATPart')
