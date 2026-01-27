# CATIA 批量操作相关功能
from typing import Dict, Any, List
import os


class BatchFeature:
    def __init__(self, service):
        self.service = service

    def set_parameters_batch(self, params: Dict[str, Any]) -> Dict[str, Any]:
        results = {}
        if not self.service.parameters:
            return {k: 'No parameters object' for k in params}
        for name, value in params.items():
            try:
                param = self.service.parameters.item(name)
                param.value = value
                results[name] = 'ok'
            except Exception as e:
                results[name] = f'fail: {e}'
        return results

    def export_documents_batch(self, file_paths: List[str], export_dir: str) -> Dict[str, Any]:
        results = {}
        for file_path in file_paths:
            try:
                doc = self.service.documents.open(file_path)
                base = os.path.basename(file_path)
                export_path = os.path.join(export_dir, base)
                doc.save_as(export_path)
                doc.close()
                results[file_path] = 'ok'
            except Exception as e:
                results[file_path] = f'fail: {e}'
        return results
