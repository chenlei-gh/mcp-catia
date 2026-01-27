# CATIA 参数化与属性、复杂操作与导出、B-Rep/Hybrid等功能
from typing import Any


class ParamFeature:
    def __init__(self, service):
        self.service = service

    def set_parameter(self, name: str, value: Any) -> str:
        try:
            if not self.service.parameters:
                return 'fail: no parameters object'
            param = self.service.parameters.item(name)
            param.value = value
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def get_parameter(self, name: str) -> Any:
        try:
            if not self.service.parameters:
                return 'fail: no parameters object'
            param = self.service.parameters.item(name)
            return param.value
        except Exception as e:
            return f'fail: {e}'

    def get_part_property(self, prop: str) -> Any:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            return getattr(self.service.part, prop, 'fail: property not found')
        except Exception as e:
            return f'fail: {e}'

    def set_part_property(self, prop: str, value: Any) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            setattr(self.service.part, prop, value)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def link_parameter(self, target: str, source: str) -> str:
        try:
            if not self.service.parameters:
                return 'fail: no parameters object'
            t = self.service.parameters.item(target)
            s = self.service.parameters.item(source)
            t.value = s.value
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def measure_body(self) -> Any:
        try:
            if not self.service.measure:
                return 'fail: no measure object'
            return self.service.measure.get_body_measure()
        except Exception as e:
            return f'fail: {e}'

    def measure_face(self, face_ref: Any) -> Any:
        try:
            if not self.service.measure:
                return 'fail: no measure object'
            return self.service.measure.get_face_measure(face_ref)
        except Exception as e:
            return f'fail: {e}'

    def measure_edge(self, edge_ref: Any) -> Any:
        try:
            if not self.service.measure:
                return 'fail: no measure object'
            return self.service.measure.get_edge_measure(edge_ref)
        except Exception as e:
            return f'fail: {e}'

    def export_drawing(self, file_path: str) -> str:
        try:
            if not self.service.drawing:
                return 'fail: no drawing loaded'
            self.service.drawing.save_as(file_path)
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def get_brep(self) -> Any:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            return self.service.part.get_brep()
        except Exception as e:
            return f'fail: {e}'

    def edit_hybrid_body(self, name: str, op: str, *args) -> str:
        try:
            if not self.service.hybrid_bodies:
                return 'fail: no hybrid_bodies object'
            hb = self.service.hybrid_bodies.item(name)
            if op == 'add':
                # 伪代码，实际pycatia需支持
                hb.add(*args)
            elif op == 'remove':
                hb.remove(*args)
            else:
                return 'fail: unsupported op'
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'
