# CATIA 装配与层级操作相关功能
from typing import Any


class AssemblyFeature:
    def __init__(self, service):
        self.service = service

    def create_product(self, name: str = "Product1") -> str:
        try:
            if not self.service.documents:
                return 'fail: CATIA未连接'
            product_doc = self.service.documents.add("Product")
            product_doc.product.name = name
            self.service.product = product_doc.product
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def add_part(self, part_path: str) -> str:
        try:
            if not self.service.product:
                return 'fail: no product loaded'
            self.service.product.products.add_component(part_path)
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def remove_part(self, index: int) -> str:
        try:
            if not self.service.product:
                return 'fail: no product loaded'
            if index < 1 or index > self.service.product.products.count:
                return 'fail: index out of range'
            self.service.product.products.remove(index)
            return 'ok'
        except Exception as e:
            return f'fail: {e}'

    def add_constraint(self, type_: str, ref1: Any, ref2: Any) -> str:
        try:
            if not self.service.product:
                return 'fail: no product loaded'
            constraints = self.service.product.constraints
            if type_ == 'coincident':
                constraints.add_coincidence(ref1, ref2)
            elif type_ == 'contact':
                constraints.add_contact(ref1, ref2)
            elif type_ == 'offset':
                constraints.add_offset(ref1, ref2, 0)
            else:
                return 'fail: unsupported constraint type'
            return 'ok'
        except Exception as e:
            return f'fail: {e}'
