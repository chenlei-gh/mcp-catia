
# CATIA MCP 服务


基于 [pycatia](https://github.com/evereux/pycatia) 的 CATIA 自动化 REST API 服务。
支持模块化建模、AI/知识驱动建模、API分层、异步任务、权限控制、Swagger文档、自动化测试与CI。

## 目录结构


```
catia_mcp_service/
  app.py                # 主程序入口
  service.py            # CATIA服务底层
  di.py                 # 服务工厂/依赖注入
  api_utils.py          # API异常/日志装饰器
  permissions.py        # 权限控制
  schemas.py            # pydantic参数校验
  swagger.py            # Swagger/OpenAPI集成
  i18n.py               # 国际化
  features/             # 各功能模块
    sketch.py           # 草图建模
    feature3d.py        # 三维特征
    object_ops.py       # 对象操作
    export.py           # 导出/图片
    batch.py            # 批量操作
    param_ops.py        # 参数/属性/测量
    assembly.py         # 装配
    template.py         # 智能模板建模
    advanced.py         # 复杂特征
    history.py          # 建模历史/撤销
    ai_suggester.py     # AI/知识驱动建模
  api_sketch.py         # API分层示例
  api_ai.py             # AI建模API
  async_tasks.py        # 异步任务队列
examples/
tests/
.github/workflows/ci.yml # CI配置
requirements.txt
dev-requirements.txt
README.md
```

## 安装

1. 克隆仓库
   ```bash
   git clone <repo-url>
   cd mcp-catia_
   ```
2. 安装依赖
   ```bash
   pip install -r requirements.txt
   pip install -r dev-requirements.txt  # 可选，开发/测试
   ```

## 快速开始


```bash
python -m catia_mcp_service.app
```

## 依赖

详见 requirements.txt 和 dev-requirements.txt。

# 主要功能

- 完整的 CATIA 建模与装配 API（草图、三维特征、装配、参数、测量、导出等）
- 智能参数化建模模板（如法兰一键建模）
- 复杂特征（壳体、肋、筋、拔模、扫掠、放样等）
- AI/知识驱动建模（自然语言转建模、标准件库自动建模）
- API分层、依赖注入、统一异常与日志
- JWT权限控制、细粒度角色管理
- 异步任务队列、批量建模
- Swagger/OpenAPI自动文档与在线调试
- pydantic参数校验、类型提示
- 国际化与多语言支持
- 单元测试/集成测试、CI自动化

## 典型API

- /api/sketch/create         创建草图
- /api/feature3d/pad        拉伸特征
- /api/assembly/add_part    装配添加零件
- /api/template/flange      智能法兰建模
- /api/ai/modeling          AI自然语言建模
- /api/ai/knowledge         标准件库建模
- /api/image/capture        视图截图
- /api/batch/set_parameters 批量参数设置

更多API见 features/ 目录与 Swagger 文档。

## 示例

见 examples/ 目录，或参考 tests/ 单元测试。

## 前端/SDK调用

详见 README 末尾“API路由与调用样例”或参考 api_ai.py、api_sketch.py。


## 贡献

欢迎 issue 和 PR！建议先阅读 CONTRIBUTING.md（如有）。

## License

MIT

---

## API路由与调用样例

### Python SDK
```python
import requests
token = 'your-jwt-token'
base_url = 'http://localhost:5000'
headers = {'Authorization': f'Bearer {token}'}
params = {'outer_diameter': 100, 'inner_diameter': 50, 'thickness': 10, 'hole_count': 8, 'hole_diameter': 10, 'hole_circle_diameter': 80}
resp = requests.post(f'{base_url}/api/template/flange', json=params, headers=headers)
print(resp.json())
```

### 前端 fetch
```js
fetch('/api/template/flange', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
  },
  body: JSON.stringify({
    outer_diameter: 100,
    inner_diameter: 50,
    thickness: 10,
    hole_count: 8,
    hole_diameter: 10,
    hole_circle_diameter: 80
  })
}).then(res => res.json()).then(console.log)
```

### 8. 分析操作
- 质量分析
- 干涉检查

### 9. 工程图操作
- 创建视图
- 添加尺寸

### 10. 系统操作
- 获取系统信息

## 安装要求

- Python 3.8+
- CATIA V5/V6
- pycatia 0.8.2+
- 其他依赖见requirements.txt

## 安装步骤

1. 克隆仓库：
```bash
git clone [repository_url]
cd catia-mcp-service
```

2. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 配置环境变量：
- 复制`.env.example`为`.env`
- 修改配置参数

## 运行服务

```bash
python catia_mcp_service.py
```

服务将在 http://localhost:5000 启动

## API使用示例

### 1. 连接CATIA
```python
import requests

# 获取JWT令牌
response = requests.post('http://localhost:5000/api/catia/connect', 
                        headers={'Authorization': f'Bearer {token}'})
```

### 2. 创建新文档
```python
response = requests.post('http://localhost:5000/api/catia/document',
                        json={
                            'operation': 'create',
                            'doc_type': 'Part'
                        },
                        headers={'Authorization': f'Bearer {token}'})
```

### 3. 创建几何体
```python
# 创建点
response = requests.post('http://localhost:5000/api/catia/geometry',
                        json={
                            'operation': 'point',
                            'x': 0,
                            'y': 0,
                            'z': 0
                        },
                        headers={'Authorization': f'Bearer {token}'})
```

## API文档

### 认证
所有API请求都需要在header中包含JWT令牌：
```
Authorization: Bearer <token>
```

### 主要端点

1. 连接CATIA
- POST `/api/catia/connect`

2. 文档操作
- POST `/api/catia/document`
  - operation: open/save/create/close

3. 参数操作
- GET `/api/catia/parameters`
- POST `/api/catia/parameters`

4. 几何操作
- POST `/api/catia/geometry`
  - operation: point/line/plane

5. 草图操作
- POST `/api/catia/sketch`
  - operation: create/add_line/add_circle

6. 特征操作
- POST `/api/catia/feature`
  - operation: pad/pocket/revolution

7. 装配操作
- POST `/api/catia/assembly`
  - operation: add_component/create_constraint

8. 测量操作
- POST `/api/catia/measure`
  - operation: distance/angle/area/volume

9. 分析操作
- POST `/api/catia/analysis`
  - operation: mass/interference

10. 工程图操作
- POST `/api/catia/drawing`
  - operation: create_view/add_dimension

11. 系统操作
- GET `/api/catia/system`

## 错误处理

所有API响应都遵循以下格式：
```json
{
    "status": "success/error",
    "message": "操作结果描述",
    "data": {} // 可选，成功时返回的数据
}
```

## 日志

服务运行日志保存在`catia_mcp.log`文件中，包含以下信息：
- 时间戳
- 日志级别
- 模块名
- 消息内容

## 注意事项

1. 确保CATIA已正确安装并可以正常运行
2. 使用前请先获取JWT令牌
3. 所有API调用都需要包含认证信息
4. 注意处理API返回的错误信息

## 贡献指南

1. Fork项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 许可证

MIT License

## 联系方式

如有问题，请提交Issue或联系维护者。 