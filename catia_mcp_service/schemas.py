# 参数校验与类型提示（pydantic示例）
from pydantic import BaseModel, Field


class SketchCreateModel(BaseModel):
    plane: str = Field(..., description="平面名，如xy_plane")


class PadModel(BaseModel):
    sketch_name: str
    length: float


# 其他API参数模型同理
