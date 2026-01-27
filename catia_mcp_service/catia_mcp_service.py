"""
CATIA MCP Service - Backward compatibility module

This module re-exports CATIAService from service.py for backward compatibility.
The main implementation is in service.py.
"""

from catia_mcp_service.service import CATIAService

__all__ = ['CATIAService']
