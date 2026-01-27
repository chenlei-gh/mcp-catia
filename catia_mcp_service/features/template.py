# 智能参数化建模模板示例
from typing import Dict, Any


class TemplateFeature:
    def __init__(self, service):
        self.service = service

    def create_flange(self, params: Dict[str, Any]) -> str:
        """
        params: {
            'outer_diameter': float,
            'inner_diameter': float,
            'thickness': float,
            'hole_count': int,
            'hole_diameter': float,
            'hole_circle_diameter': float
        }
        """
        try:
            # 1. 创建圆形草图
            sketch_name = 'flange_sketch'
            sf = self.service.sketch_feature
            sf.create_sketch('xy_plane')
            sf.draw_circle(sketch_name, 0, 0, params['outer_diameter'] / 2)
            sf.draw_circle(sketch_name, 0, 0, params['inner_diameter'] / 2)
            # 2. 拉伸成型
            f3d = self.service.feature3d
            f3d.pad(sketch_name, params['thickness'])
            # 3. 阵列布孔
            for i in range(params['hole_count']):
                import math

                angle = 2 * math.pi * i / params['hole_count']
                x = params['hole_circle_diameter'] / 2 * math.cos(angle)
                y = params['hole_circle_diameter'] / 2 * math.sin(angle)
                sf.draw_circle(sketch_name, x, y, params['hole_diameter'] / 2)
            # 4. 拉伸切除孔
            f3d.pocket(sketch_name, params['thickness'] + 1)
            return 'ok'
        except Exception as e:
            return f'fail: {e}'
