import pytest

def test_import_service():
    try:
        from catia_mcp_service.catia_mcp_service import CATIAService
    except ImportError:
        pytest.fail('CATIAService import failed')

def test_service_instance():
    from catia_mcp_service.catia_mcp_service import CATIAService
    service = CATIAService()
    assert service is not None
