# 复杂特征与高级操作示例
class AdvancedFeature:
    def __init__(self, service):
        self.service = service

    def shell(self, thickness: float) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            _ = self.service.part.shape_factory.add_new_shell(thickness)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def rib(self, sketch_name: str, thickness: float) -> str:
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            _ = self.service.part.shape_factory.add_new_rib(sketch, thickness)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def stiffener(self, edge_ref, thickness: float) -> str:
        try:
            _ = self.service.part.shape_factory.add_new_stiffener(edge_ref, thickness)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def draft(self, face_ref, angle: float) -> str:
        try:
            _ = self.service.part.shape_factory.add_new_draft(face_ref, angle)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def sweep(self, guide_sketch: str, section_sketch: str) -> str:
        try:
            guide = self._find_sketch(guide_sketch)
            section = self._find_sketch(section_sketch)
            if not guide or not section:
                return 'fail: sketch not found'
            _ = self.service.part.shape_factory.add_new_sweep(guide, section)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def loft(self, section_sketches: list) -> str:
        try:
            sections = [self._find_sketch(s) for s in section_sketches]
            if not all(sections):
                return 'fail: some sketch not found'
            _ = self.service.part.shape_factory.add_new_loft(sections)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def _find_sketch(self, sketch_name: str):
        if not self.service.part or not self.service.part.sketches:
            return None
        for s in self.service.part.sketches:
            if s.name == sketch_name:
                return s
        return None
