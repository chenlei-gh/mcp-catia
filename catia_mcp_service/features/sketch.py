# CATIA 草图与几何建模相关功能


class SketchFeature:
    def __init__(self, service):
        self.service = service

    def create_sketch(self, plane_name: str) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            plane = getattr(self.service.part.origin_elements, plane_name, None)
            if not plane:
                return f'fail: plane {plane_name} not found'
            sketches = self.service.part.sketches
            sketch = sketches.add(plane)
            self.service.part.update()
            return sketch.name
        except Exception as e:
            return f'fail: {e}'

    def draw_point(self, sketch_name: str, x: float, y: float) -> str:
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            factory = sketch.open_edition()
            factory.create_point(x, y)
            sketch.close_edition()
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def draw_line(self, sketch_name: str, x1: float, y1: float, x2: float, y2: float) -> str:
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            factory = sketch.open_edition()
            factory.create_line(x1, y1, x2, y2)
            sketch.close_edition()
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def draw_circle(self, sketch_name: str, x: float, y: float, r: float) -> str:
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            factory = sketch.open_edition()
            factory.create_circle(x, y, r)
            sketch.close_edition()
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def draw_rectangle(self, sketch_name: str, x: float, y: float, w: float, h: float) -> str:
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            factory = sketch.open_edition()
            factory.create_line(x, y, x + w, y)
            factory.create_line(x + w, y, x + w, y + h)
            factory.create_line(x + w, y + h, x, y + h)
            factory.create_line(x, y + h, x, y)
            sketch.close_edition()
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def draw_ellipse(self, sketch_name: str, x: float, y: float, rx: float, ry: float) -> str:
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            factory = sketch.open_edition()
            factory.create_ellipse(x, y, rx, ry)
            sketch.close_edition()
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def draw_polyline(self, sketch_name: str, points: list) -> str:
        """points: [(x1, y1), (x2, y2), ...]"""
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch or len(points) < 2:
                return 'fail: invalid input'
            factory = sketch.open_edition()
            for i in range(len(points) - 1):
                x1, y1 = points[i]
                x2, y2 = points[i + 1]
                factory.create_line(x1, y1, x2, y2)
            sketch.close_edition()
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def draw_spline(self, sketch_name: str, points: list) -> str:
        """points: [(x1, y1), (x2, y2), ...]"""
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch or len(points) < 2:
                return 'fail: invalid input'
            factory = sketch.open_edition()
            factory.create_spline(points)
            sketch.close_edition()
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def mirror_elements(self, sketch_name: str, element_indices: list, axis_index: int) -> str:
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            factory = sketch.open_edition()
            elems = sketch.projection_elements
            axis = elems.item(axis_index + 1)
            for idx in element_indices:
                elem = elems.item(idx + 1)
                factory.mirror_element(elem, axis)
            sketch.close_edition()
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def array_elements(self, sketch_name: str, element_indices: list, count: int, dx: float, dy: float) -> str:
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            factory = sketch.open_edition()
            elems = sketch.projection_elements
            for idx in element_indices:
                elem = elems.item(idx + 1)
                factory.array_element(elem, count, dx, dy)
            sketch.close_edition()
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def add_constraints_batch(self, sketch_name: str, constraints: list) -> str:
        """constraints: [(type, args), ...]"""
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            cons = sketch.constraints
            for ctype, args in constraints:
                if ctype == 'distance':
                    cons.add_distance(*args)
                elif ctype == 'coincidence':
                    cons.add_coincidence(*args)
                elif ctype == 'parallel':
                    cons.add_parallel(*args)
                elif ctype == 'perpendicular':
                    cons.add_perpendicular(*args)
                elif ctype == 'equal_length':
                    cons.add_equal_length(*args)
                elif ctype == 'equal_radius':
                    cons.add_equal_radius(*args)
                elif ctype == 'symmetry':
                    cons.add_symmetry(*args)
                # 可扩展更多类型
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def group_elements(self, sketch_name: str, element_indices: list) -> str:
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            factory = sketch.open_edition()
            elems = sketch.projection_elements
            group = factory.create_group()
            for idx in element_indices:
                elem = elems.item(idx + 1)
                group.add_element(elem)
            sketch.close_edition()
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def project_geometry(self, sketch_name: str, target_name: str) -> str:
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            factory = sketch.open_edition()
            target = self._find_sketch(target_name)
            if not target:
                return 'fail: target not found'
            factory.project_geometry(target)
            sketch.close_edition()
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def set_element_property(
        self, sketch_name: str, element_index: int, color: str = None, linetype: str = None, layer: int = None
    ) -> str:
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            elems = sketch.projection_elements
            elem = elems.item(element_index + 1)
            if color:
                elem.color = color
            if linetype:
                elem.linetype = linetype
            if layer is not None:
                elem.layer = layer
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def delete_sketch_element(self, sketch_name: str, element_index: int) -> str:
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            factory = sketch.open_edition()
            elems = sketch.projection_elements
            if element_index < 0 or element_index >= elems.count:
                return 'fail: index out of range'
            elem = elems.item(element_index + 1)
            factory.delete_element(elem)
            sketch.close_edition()
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def add_constraint(self, sketch_name: str, constraint_type: str, *args) -> str:
        try:
            sketch = self._find_sketch(sketch_name)
            if not sketch:
                return 'fail: sketch not found'
            constraints = sketch.constraints
            if constraint_type == 'distance':
                constraints.add_distance(*args)
            elif constraint_type == 'coincidence':
                constraints.add_coincidence(*args)
            else:
                return 'fail: unsupported constraint type'
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
