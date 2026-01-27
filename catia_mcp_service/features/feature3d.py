# CATIA 三维特征建模相关功能
from typing import Any


class Feature3D:
    def __init__(self, service):
        self.service = service

    def sweep(self, profile_sketch: str, guide_sketch: str) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            profile = self._find_sketch(profile_sketch)
            guide = self._find_sketch(guide_sketch)
            if not profile or not guide:
                return 'fail: sketch not found'
            _ = self.service.part.shape_factory.add_new_rib(profile, guide)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def loft(self, section_sketches: list) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            sections = [self._find_sketch(name) for name in section_sketches]
            if not all(sections):
                return 'fail: some sketches not found'
            _ = self.service.part.shape_factory.add_new_loft(sections)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def add_body(self, name: str = None) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            body = self.service.part.bodies.add()
            if name:
                body.name = name
            self.service.part.update()
            return body.name
        except Exception as e:
            return f'fail: {e}'

    def set_current_body(self, name: str) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            for b in self.service.part.bodies:
                if b.name == name:
                    self.service.part.in_work_object = b
                    return 'ok'
            return 'fail: body not found'
        except Exception as e:
            return f'fail: {e}'

    def boolean_operation(self, op_type: str, body1: str, body2: str) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            b1 = None
            b2 = None
            for b in self.service.part.bodies:
                if b.name == body1:
                    b1 = b
                if b.name == body2:
                    b2 = b
            if not b1 or not b2:
                return 'fail: body not found'
            if op_type == 'union':
                self.service.part.shape_factory.add_new_add(b1, b2)
            elif op_type == 'subtract':
                self.service.part.shape_factory.add_new_remove(b1, b2)
            elif op_type == 'intersect':
                self.service.part.shape_factory.add_new_intersect(b1, b2)
            else:
                return 'fail: unsupported op_type'
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def advanced_hole(self, point_ref: Any, depth: float, diameter: float = None, type_: str = None) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            hole = self.service.part.shape_factory.add_new_hole(point_ref, depth)
            if diameter:
                hole.diameter = diameter
            if type_:
                hole.type = type_
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def advanced_chamfer(self, edge_ref: Any, length: float, angle: float, mode: str = None) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            chamfer = self.service.part.shape_factory.add_new_chamfer(edge_ref, length, angle)
            if mode:
                chamfer.mode = mode
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def advanced_fillet(self, edge_ref: Any, radius: float, type_: str = None) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            fillet = self.service.part.shape_factory.add_new_fillet(edge_ref, radius)
            if type_:
                fillet.type = type_
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def pad(self, sketch_name: str, length: float) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            _ = self.service.part.shape_factory.add_new_pad(sketch, length)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def pocket(self, sketch_name: str, length: float) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            _ = self.service.part.shape_factory.add_new_pocket(sketch, length)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def shaft(self, sketch_name: str, angle: float) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            _ = self.service.part.shape_factory.add_new_shaft(sketch, angle)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def groove(self, sketch_name: str, angle: float) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            _ = self.service.part.shape_factory.add_new_groove(sketch, angle)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def hole(self, point_ref: Any, depth: float) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            _ = self.service.part.shape_factory.add_new_hole(point_ref, depth)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def chamfer(self, edge_ref: Any, length: float, angle: float) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            _ = self.service.part.shape_factory.add_new_chamfer(edge_ref, length, angle)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def fillet(self, edge_ref: Any, radius: float) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            _ = self.service.part.shape_factory.add_new_fillet(edge_ref, radius)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def mirror(self, feature_ref: Any, plane_ref: Any) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            _ = self.service.part.shape_factory.add_new_mirror(feature_ref, plane_ref)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def pattern(self, feature_ref: Any, count: int, spacing: float) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            _ = self.service.part.shape_factory.add_new_pattern(feature_ref, count, spacing)
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
