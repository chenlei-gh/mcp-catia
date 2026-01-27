# CATIA 文件导出与图片相关功能


class ExportFeature:
    def __init__(self, service):
        self.service = service

    def export_to_format(self, file_path: str, export_path: str, fmt: str) -> str:
        try:
            doc = self.service.documents.open(file_path)
            if fmt.lower() == 'step':
                doc.save_as(export_path + '.step')
            elif fmt.lower() == 'iges':
                doc.save_as(export_path + '.iges')
            elif fmt.lower() == 'stl':
                doc.save_as(export_path + '.stl')
            else:
                return f'fail: unsupported format {fmt}'
            doc.close()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def capture_image(self, file_path: str = 'catia_capture.png', fmt: str = 'png') -> str:
        try:
            if not self.service.catia or not hasattr(self.service.catia, 'active_window'):
                return 'fail: CATIA未连接或无活动窗口'
            win = self.service.catia.active_window
            if fmt.lower() not in ('png', 'jpg', 'jpeg', 'bmp'):
                return 'fail: 不支持的图片格式'
            win.capture_to_file(file_path)
            return file_path
        except Exception as e:
            return f'fail: {e}'
