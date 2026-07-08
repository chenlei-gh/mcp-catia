# CATIA MCP Service

<div align="center">

```
 ██████╗ █████╗ ████████╗██╗ █████╗     ███╗   ███╗ ██████╗██████╗
██╔════╝██╔══██╗╚══██╔══╝██║██╔══██╗    ████╗ ████║██╔════╝██╔══██╗
██║     ███████║   ██║   ██║███████║    ██╔████╔██║██║     ██████╔╝
██║     ██╔══██║   ██║   ██║██╔══██║    ██║╚██╔╝██║██║     ██╔═══╝
╚██████╗██║  ██║   ██║   ██║██║  ██║    ██║ ╚═╝ ██║╚██████╗██║
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝╚═╝

   CATIA Automation REST API · Powered by pycatia
```

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

> A comprehensive CATIA automation REST API service built on [pycatia](https://github.com/evereux/pycatia). Modular modeling, AI-driven design, layered API, async tasks, JWT auth, Swagger docs, CI/CD.

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

Service starts at `http://localhost:5000` → Swagger UI at `/api/docs`

---

### 🧩 Core Features

| <!-- --> | <!-- --> |
|---|---|
| 🎨 **Sketch & 3D** | Sketch creation, Pad, Pocket, Revolution, Hole, Rib, Shell, Draft, Sweep, Loft |
| 🔧 **Assembly** | Add components, constraints, positioning |
| 📏 **Parameters & Measure** | Read/write parameters, distance, angle, area, volume, mass |
| 🤖 **AI Modeling** | Natural language → CATIA model, knowledge-based standard parts |
| 🧠 **Smart Templates** | One-click parametric modeling (e.g. flange, gear) |
| 📸 **Export & Capture** | Screenshots, STL, STEP export |
| 🔐 **JWT Auth** | Token-based access control with role permissions |
| ⚙️ **Async Tasks** | Background batch processing, progress tracking |
| 📖 **Swagger** | Auto-generated OpenAPI docs, online testing |
| 🌍 **i18n** | Multi-language support (EN / ZH) |

---

### 📡 API Overview

```
POST  /api/connect              Connect to CATIA
POST  /api/document             Create / open / save / close document
POST  /api/sketch               Create sketch, add lines, circles
POST  /api/feature3d            Pad, pocket, revolution, hole...
POST  /api/assembly             Add component, constraint
POST  /api/template             Smart parametric modeling (flange, gear...)
POST  /api/ai/modeling          Natural language → model
POST  /api/ai/knowledge         Standard parts library
POST  /api/measure              Distance, angle, area, volume, mass
POST  /api/image/capture        View screenshot
POST  /api/batch                Batch parameter setting
GET   /api/system               System info
```

> Full API docs: open `/api/docs` after startup

---

### 🐍 Quick Examples

#### Create a sketch and pad

```python
import requests
from requests.auth import HTTPBasicAuth

BASE = "http://localhost:5000"
auth = HTTPBasicAuth("admin", "admin")

# Connect CATIA
requests.post(f"{BASE}/api/connect", auth=auth)

# Create part document
requests.post(f"{BASE}/api/document",
    json={"operation": "create", "doc_type": "Part"}, auth=auth)

# Create sketch
requests.post(f"{BASE}/api/sketch",
    json={"operation": "create", "plane": "xy"}, auth=auth)

# Add circle
requests.post(f"{BASE}/api/sketch",
    json={"operation": "add_circle", "center": [0, 0], "radius": 50}, auth=auth)

# Pad
requests.post(f"{BASE}/api/feature3d",
    json={"operation": "pad", "length": 20}, auth=auth)
```

#### Smart flange in one call

```python
requests.post(f"{BASE}/api/template/flange", json={
    "outer_diameter": 100, "inner_diameter": 50,
    "thickness": 10, "hole_count": 8,
    "hole_diameter": 10, "hole_circle_diameter": 80
}, auth=auth)
```

#### AI natural language modeling

```python
requests.post(f"{BASE}/api/ai/modeling", json={
    "prompt": "Create a 100x50mm plate with 4 corner holes of 10mm diameter"
}, auth=auth)
```

---

### 🏗️ Project Structure

```
mcp-catia/
├── catia_mcp_service/
│   ├── app.py               # Main entry
│   ├── service.py            # CATIA COM core
│   ├── features/             # Feature modules
│   │   ├── sketch.py         # Sketches
│   │   ├── feature3d.py      # 3D features
│   │   ├── assembly.py       # Assembly
│   │   ├── object_ops.py     # Object CRUD
│   │   ├── batch.py          # Batch ops
│   │   ├── param_ops.py      # Parameters
│   │   ├── export.py         # Export / capture
│   │   ├── template.py       # Smart templates
│   │   ├── advanced.py       # Complex features
│   │   ├── history.py        # Undo / history
│   │   └── ai_suggester.py   # AI suggestions
│   ├── di.py                 # Dependency injection
│   ├── permissions.py        # JWT + RBAC
│   ├── schemas.py            # Pydantic validation
│   ├── swagger.py            # OpenAPI integration
│   ├── i18n.py               # Internationalization
│   └── async_tasks.py        # Async queue
├── examples/                 # Usage examples
├── tests/                    # Test suite
└── .github/workflows/ci.yml  # CI/CD
```

---

### 📦 Requirements

| Dependency | Version |
|---|---|
| Python | 3.8+ |
| CATIA | V5 / V6 |
| pycatia | 0.8.2+ |

See `requirements.txt` for full list.

---

> [🌐 中文](#chinese)

---

<a name="chinese"></a>

## 🇨🇳 中文

> 基于 [pycatia](https://github.com/evereux/pycatia) 的 CATIA 自动化 REST API 服务。模块化建模、AI 驱动设计、分层 API、异步任务、JWT 鉴权、Swagger 文档、CI/CD。

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

服务启动于 `http://localhost:5000` → Swagger 文档位于 `/api/docs`

---

### 🧩 核心功能

| <!-- --> | <!-- --> |
|---|---|
| 🎨 **草图与三维特征** | 草图创建、拉伸、挖槽、旋转、孔、肋、壳、拔模、扫掠、放样 |
| 🔧 **装配** | 添加零件、约束、定位 |
| 📏 **参数与测量** | 参数读写、距离、角度、面积、体积、质量 |
| 🤖 **AI 建模** | 自然语言转 CATIA 模型、知识驱动标准件建模 |
| 🧠 **智能模板** | 一键参数化建模（法兰、齿轮等） |
| 📸 **导出与截图** | 视图截图、STL/STEP 导出 |
| 🔐 **JWT 鉴权** | Token 认证 + 角色权限控制 |
| ⚙️ **异步任务** | 后台批量处理、进度追踪 |
| 📖 **Swagger** | 自动生成 OpenAPI 文档，在线调试 |
| 🌍 **国际化** | 中英文多语言支持 |

---

### 📡 API 概览

```
POST  /api/connect              连接 CATIA
POST  /api/document             创建/打开/保存/关闭文档
POST  /api/sketch               创建草图、添加直线、圆
POST  /api/feature3d            拉伸、挖槽、旋转、孔...
POST  /api/assembly             添加组件、约束
POST  /api/template             智能参数化建模（法兰、齿轮...）
POST  /api/ai/modeling          自然语言 → 模型
POST  /api/ai/knowledge         标准件库建模
POST  /api/measure              距离、角度、面积、体积、质量
POST  /api/image/capture        视图截图
POST  /api/batch                批量参数设置
GET   /api/system               系统信息
```

> 完整 API 文档：启动后访问 `/api/docs`

---

### 🐍 快速示例

#### 创建草图并拉伸

```python
import requests
from requests.auth import HTTPBasicAuth

BASE = "http://localhost:5000"
auth = HTTPBasicAuth("admin", "admin")

# 连接 CATIA
requests.post(f"{BASE}/api/connect", auth=auth)

# 创建零件文档
requests.post(f"{BASE}/api/document",
    json={"operation": "create", "doc_type": "Part"}, auth=auth)

# 创建草图
requests.post(f"{BASE}/api/sketch",
    json={"operation": "create", "plane": "xy"}, auth=auth)

# 添加圆
requests.post(f"{BASE}/api/sketch",
    json={"operation": "add_circle", "center": [0, 0], "radius": 50}, auth=auth)

# 拉伸
requests.post(f"{BASE}/api/feature3d",
    json={"operation": "pad", "length": 20}, auth=auth)
```

#### 一键智能法兰

```python
requests.post(f"{BASE}/api/template/flange", json={
    "outer_diameter": 100, "inner_diameter": 50,
    "thickness": 10, "hole_count": 8,
    "hole_diameter": 10, "hole_circle_diameter": 80
}, auth=auth)
```

#### AI 自然语言建模

```python
requests.post(f"{BASE}/api/ai/modeling", json={
    "prompt": "创建一块 100x50mm 的板，四个角各有一个直径 10mm 的孔"
}, auth=auth)
```

---

### 📦 依赖

| 依赖 | 版本 |
|---|---|
| Python | 3.8+ |
| CATIA | V5 / V6 |
| pycatia | 0.8.2+ |

完整列表见 `requirements.txt`。

---

> [🇬🇧 English](#english)

---

<div align="center">

## 📜 License

MIT — see [LICENSE](LICENSE)

<br>

**[Issues](https://github.com/chenlei-gh/mcp-catia/issues) · [Examples](examples/) · [Tests](tests/)**

</div>
