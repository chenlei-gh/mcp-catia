# CATIA 对象操作相关功能
from typing import Any


class ObjectFeature:
    def __init__(self, service):
        self.service = service

    def list_assembly_tree(self) -> Any:
        try:
            if not self.service.product:
                return 'fail: no product loaded'

            def walk(prod):
                node = {'name': prod.name, 'children': []}
                for i in range(1, prod.products.count + 1):
                    child = prod.products.item(i)
                    node['children'].append(walk(child))
                return node

            return walk(self.service.product)
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

    def set_material(self, material_name: str) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            # 伪代码，实际pycatia需支持材料库API
            self.service.part.material = material_name
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def set_color(self, r: int, g: int, b: int) -> str:
        try:
            if not self.service.part:
                return 'fail: no part loaded'
            # 伪代码，实际pycatia需支持颜色API
            self.service.part.color = (r, g, b)
            self.service.part.update()
            return 'ok'
        except Exception as e:
            return f'fail: {e}'
