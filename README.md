# CATIA MCP Service

<div align="center">

<h1>🔧 CATIA MCP</h1>

**CATIA Automation REST API · Powered by pycatia**

<br>

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![CATIA](https://img.shields.io/badge/CATIA-V5%20%7C%20V6-orange)]()
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Swagger](https://img.shields.io/badge/docs-Swagger-brightgreen)]()

<br>

🌐 [English](#english) | [中文](#chinese)

</div>

---

<a name="english"></a>

## 🇬🇧 English

> Comprehensive CATIA automation REST API built on [pycatia](https://github.com/evereux/pycatia). Features modular modeling, AI-driven design, JWT auth, Swagger docs, and async task processing.

---

### ⚡ Quick Start

```bash
# Clone & install
git clone https://github.com/chenlei-gh/mcp-catia.git
cd mcp-catia
pip install -r requirements.txt

# Run
python -m catia_mcp_service.app
```

**Service URL:** `http://localhost:5000`  
**Swagger Docs:** `http://localhost:5000/api/docs`

---

### 🎯 Core Features

**🎨 Modeling**
- Sketch creation (lines, circles, rectangles, splines)
- 3D features: Pad, Pocket, Revolution, Hole, Rib, Shell
- Advanced: Draft, Sweep, Loft, Pattern

**🔧 Assembly & Parameters**
- Component positioning and constraints
- Read/write parameters, relations
- Batch parameter updates

**🤖 AI & Automation**
- Natural language → CATIA models
- Smart templates (flange, gear, standard parts)
- Knowledge-driven modeling

**⚙️ System**
- JWT token authentication
- Role-based access control
- Async task queue
- Swagger/OpenAPI documentation
- Multi-language support (EN/ZH)

---

### 📡 API Endpoints

| Category | Endpoint | Description |
|----------|----------|-------------|
| **Connection** | `POST /api/connect` | Connect to CATIA |
| **Document** | `POST /api/document` | Create/open/save/close |
| **Sketch** | `POST /api/sketch` | Create sketch, add geometry |
| **3D Feature** | `POST /api/feature3d` | Pad, pocket, hole, etc. |
| **Assembly** | `POST /api/assembly` | Add parts, constraints |
| **Template** | `POST /api/template` | Smart parametric models |
| **AI** | `POST /api/ai/modeling` | Natural language modeling |
| **Measure** | `POST /api/measure` | Distance, angle, mass |
| **Export** | `POST /api/image/capture` | Screenshot, STL, STEP |
| **System** | `GET /api/system` | System information |

Full API documentation available at `/api/docs` after startup.

---

### 🐍 Examples

#### Basic: Create and extrude a circle

```python
import requests
from requests.auth import HTTPBasicAuth

BASE = "http://localhost:5000"
auth = HTTPBasicAuth("admin", "admin")

# Connect
requests.post(f"{BASE}/api/connect", auth=auth)

# Create part
requests.post(f"{BASE}/api/document",
    json={"operation": "create", "doc_type": "Part"}, 
    auth=auth)

# Sketch
requests.post(f"{BASE}/api/sketch",
    json={"operation": "create", "plane": "xy"}, 
    auth=auth)

# Circle
requests.post(f"{BASE}/api/sketch",
    json={
        "operation": "add_circle",
        "center": [0, 0],
        "radius": 50
    }, auth=auth)

# Pad
requests.post(f"{BASE}/api/feature3d",
    json={"operation": "pad", "length": 20}, 
    auth=auth)
```

#### Smart template: One-line flange

```python
requests.post(f"{BASE}/api/template/flange", 
    json={
        "outer_diameter": 100,
        "inner_diameter": 50,
        "thickness": 10,
        "hole_count": 8,
        "hole_diameter": 10,
        "hole_circle_diameter": 80
    }, auth=auth)
```

#### AI: Natural language modeling

```python
requests.post(f"{BASE}/api/ai/modeling",
    json={
        "prompt": "Create a 100x50mm plate with 4 corner holes, diameter 10mm"
    }, auth=auth)
```

---

### 🏗️ Project Structure

```
mcp-catia/
├── catia_mcp_service/
│   ├── app.py               # Main entry
│   ├── service.py           # CATIA core
│   ├── features/            # Feature modules
│   │   ├── sketch.py
│   │   ├── feature3d.py
│   │   ├── assembly.py
│   │   ├── template.py
│   │   └── ai_suggester.py
│   ├── permissions.py       # JWT auth
│   ├── schemas.py           # Validation
│   └── swagger.py           # API docs
├── examples/
├── tests/
└── requirements.txt
```

---

### 📦 Requirements

- **Python**: 3.8+
- **CATIA**: V5 or V6
- **pycatia**: 0.8.2+

See `requirements.txt` for full dependencies.

---

> [🌐 中文](#chinese)

---

<a name="chinese"></a>

## 🇨🇳 中文

> 基于 [pycatia](https://github.com/evereux/pycatia) 的 CATIA 自动化 REST API 服务。支持模块化建模、AI 驱动设计、JWT 鉴权、Swagger 文档和异步任务处理。

---

### ⚡ 快速开始

```bash
# 克隆并安装
git clone https://github.com/chenlei-gh/mcp-catia.git
cd mcp-catia
pip install -r requirements.txt

# 运行
python -m catia_mcp_service.app
```

**服务地址:** `http://localhost:5000`  
**文档地址:** `http://localhost:5000/api/docs`

---

### 🎯 核心功能

**🎨 建模**
- 草图创建（直线、圆、矩形、样条线）
- 三维特征：拉伸、挖槽、旋转、孔、肋、壳
- 高级特征：拔模、扫掠、放样、阵列

**🔧 装配与参数**
- 组件定位和约束
- 参数读写、关系式
- 批量参数更新

**🤖 AI 与自动化**
- 自然语言 → CATIA 模型
- 智能模板（法兰、齿轮、标准件）
- 知识驱动建模

**⚙️ 系统**
- JWT Token 认证
- 基于角色的权限控制
- 异步任务队列
- Swagger/OpenAPI 文档
- 多语言支持（中英文）

---

### 📡 API 端点

| 分类 | 端点 | 说明 |
|------|------|------|
| **连接** | `POST /api/connect` | 连接 CATIA |
| **文档** | `POST /api/document` | 创建/打开/保存/关闭 |
| **草图** | `POST /api/sketch` | 创建草图、添加几何 |
| **三维特征** | `POST /api/feature3d` | 拉伸、挖槽、孔等 |
| **装配** | `POST /api/assembly` | 添加零件、约束 |
| **模板** | `POST /api/template` | 智能参数化模型 |
| **AI** | `POST /api/ai/modeling` | 自然语言建模 |
| **测量** | `POST /api/measure` | 距离、角度、质量 |
| **导出** | `POST /api/image/capture` | 截图、STL、STEP |
| **系统** | `GET /api/system` | 系统信息 |

完整 API 文档见启动后的 `/api/docs`。

---

### 🐍 示例

#### 基础：创建并拉伸圆

```python
import requests
from requests.auth import HTTPBasicAuth

BASE = "http://localhost:5000"
auth = HTTPBasicAuth("admin", "admin")

# 连接
requests.post(f"{BASE}/api/connect", auth=auth)

# 创建零件
requests.post(f"{BASE}/api/document",
    json={"operation": "create", "doc_type": "Part"}, 
    auth=auth)

# 草图
requests.post(f"{BASE}/api/sketch",
    json={"operation": "create", "plane": "xy"}, 
    auth=auth)

# 圆
requests.post(f"{BASE}/api/sketch",
    json={
        "operation": "add_circle",
        "center": [0, 0],
        "radius": 50
    }, auth=auth)

# 拉伸
requests.post(f"{BASE}/api/feature3d",
    json={"operation": "pad", "length": 20}, 
    auth=auth)
```

#### 智能模板：一行法兰

```python
requests.post(f"{BASE}/api/template/flange", 
    json={
        "outer_diameter": 100,
        "inner_diameter": 50,
        "thickness": 10,
        "hole_count": 8,
        "hole_diameter": 10,
        "hole_circle_diameter": 80
    }, auth=auth)
```

#### AI：自然语言建模

```python
requests.post(f"{BASE}/api/ai/modeling",
    json={
        "prompt": "创建一块 100x50mm 的板，四角各有直径 10mm 的孔"
    }, auth=auth)
```

---

### 📦 依赖

- **Python**: 3.8+
- **CATIA**: V5 或 V6
- **pycatia**: 0.8.2+

完整依赖列表见 `requirements.txt`。

---

> [🇬🇧 English](#english)

---

<div align="center">

## 📜 License

MIT — see [LICENSE](LICENSE)

<br>

**[Issues](https://github.com/chenlei-gh/mcp-catia/issues) · [Examples](examples/) · [Tests](tests/)**

</div>
