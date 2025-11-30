# 🌐 Aplicación Web Contenerizada - Linktree Full-Stack

> **EA2 - Contenerización de una Aplicación Web**  
> Aplicación full-stack completamente contenerizada con Docker y Docker Compose

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/)

---

## 📋 Tabla de Contenidos

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Arquitectura del Sistema](#️-arquitectura-del-sistema)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Prerequisitos](#-prerequisitos)
- [Instalación y Despliegue](#-instalación-y-despliegue)
- [Configuración Detallada](#-configuración-detallada)
- [Endpoints de la API](#-endpoints-de-la-api)
- [Pruebas y Verificación](#-pruebas-y-verificación)
- [Comandos Útiles](#-comandos-útiles)
- [Autores](#-autores)

---

## 📋 Descripción del Proyecto

Aplicación web full-stack tipo **Linktree** que permite mostrar un perfil personal con enlaces a redes sociales. La información se almacena en una base de datos MySQL y se sirve a través de una API REST desarrollada en Flask.

### Componentes Principales

🎨 **Frontend (Nginx)**
- Interfaz web responsiva con HTML5, CSS3 y JavaScript vanilla
- Servidor web Nginx para servir archivos estáticos
- Diseño adaptativo con W3.CSS
- Consumo de API REST mediante Fetch API

⚙️ **Backend (Flask)**
- API REST desarrollada en Python 3.12 con Flask
- Conexión a base de datos MySQL con reintentos automáticos
- CORS habilitado para desarrollo
- Manejo robusto de errores y excepciones

💾 **Base de Datos (MySQL)**
- MySQL 8.0 para almacenamiento persistente
- Script de inicialización automática
- Volúmenes Docker para persistencia de datos
- Healthcheck para garantizar disponibilidad

---

## 🏗️ Arquitectura del Sistema

### Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────────────┐
│                         DOCKER HOST                              │
│                                                                  │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────────┐  │
│  │   Frontend   │      │   Backend    │      │   Database   │  │
│  │   (Nginx)    │─────▶│   (Flask)    │─────▶│   (MySQL)    │  │
│  │              │ HTTP │              │ SQL  │              │  │
│  │ Port: 8080   │      │ Port: 5000   │      │ Port: 3306   │  │
│  └──────────────┘      └──────────────┘      └──────────────┘  │
│         │                      │                      │         │
│         │                      │                      │         │
│  [HTML/CSS/JS]          [Python/Flask]         [MySQL 8.0]     │
│  [W3.CSS]               [CORS]                 [init.sql]      │
│  [Feather Icons]        [mysql-connector]      [Volumes]       │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │              Docker Network (bridge)                        │ │
│  │  - DNS automático entre servicios                          │ │
│  │  - Aislamiento de red del host                             │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │              Docker Volume (mysql_data)                     │ │
│  │  - Persistencia de datos de MySQL                          │ │
│  └────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Flujo de Datos

```
1. Usuario → Navegador (localhost:8080/linktree.html)
              ↓
2. Frontend (Nginx) → Sirve HTML/CSS/JS
              ↓
3. JavaScript → Fetch API (localhost:5000/getMyInfo)
              ↓
4. Backend (Flask) → Procesa request
              ↓
5. Backend → Conecta a MySQL (database:3306)
              ↓
6. MySQL → Retorna datos de user_info
              ↓
7. Backend → Formatea JSON
              ↓
8. Frontend → Recibe JSON y actualiza DOM
              ↓
9. Usuario → Ve información personalizada
```

---

## 📁 Estructura del Proyecto

```
front-back-bd/
├── 📄 docker-compose.yml          # Orquestación de servicios
├── 📄 README.md                   # Documentación del proyecto
├── 📄 INFORME_CONFIGURACION_PRUEBAS.md
├── 📄 PASOS_CONSTRUCCION_DESPLIEGUE.txt
│
├── 📂 backend/                    # Servicio Backend (Flask)
│   ├── 📄 Dockerfile              # Imagen Docker del backend
│   ├── 🐍 app.py                  # Aplicación Flask
│   ├── 📄 requirements.txt        # Dependencias Python
│   └── 📂 __pycache__/            # Cache de Python
│
├── 📂 frontend/                   # Servicio Frontend (Nginx)
│   ├── 📄 Dockerfile              # Imagen Docker del frontend
│   └── 📂 sitio/                  # Archivos web estáticos
│       ├── 🌐 linktree.html       # Página principal
│       ├── 📜 requests.js         # Lógica de consumo API
│       └── 🎨 [archivos CSS]      # Estilos
│
└── 📂 database/                   # Servicio Base de Datos (MySQL)
    ├── 📄 Dockerfile              # Imagen Docker de MySQL
    └── 📄 init.sql                # Script de inicialización
```

---

## ✅ Prerequisitos

Antes de comenzar, asegúrate de tener instalado:

### Software Requerido

1. **Docker Desktop** (versión 20.10 o superior)
   - 🪟 Windows: [Descargar Docker Desktop para Windows](https://docs.docker.com/desktop/install/windows-install/)
   - 🍎 macOS: [Descargar Docker Desktop para Mac](https://docs.docker.com/desktop/install/mac-install/)
   - 🐧 Linux: [Descargar Docker Desktop para Linux](https://docs.docker.com/desktop/install/linux-install/)

2. **Docker Compose** (incluido con Docker Desktop)

3. **Git** (opcional, para clonar el repositorio)

---

## 🚀 Instalación y Despliegue

```bash
# 1. Clonar el repositorio
git clone https://github.com/1531nana/app-contenerizar-TW.git
cd front-back-bd

# 2. Levantar todos los servicios
docker-compose up --build

# 3. Acceder a la aplicación
# Frontend: http://localhost:8080/linktree.html
# API: http://localhost:5000/getMyInfo
```
---

## 🔧 Configuración Detallada

### 1. Dockerfile - Base de Datos

**Ubicación:** `database/Dockerfile`

```dockerfile
FROM mysql:8.0

COPY init.sql /docker-entrypoint-initdb.d/
```

**Explicación técnica:**
- `FROM mysql:8.0`: Utiliza la imagen oficial de MySQL 8.0 de Docker Hub
- `COPY init.sql`: Copia el script SQL al directorio especial `/docker-entrypoint-initdb.d/`
  - **Nota:** MySQL ejecuta automáticamente todos los scripts en este directorio al primer inicio
  - Esto permite poblar la base de datos sin intervención manual

---

### 2. Dockerfile - Backend

**Ubicación:** `backend/Dockerfile`

```dockerfile
FROM python:3.12-alpine3.17

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
```

**Explicación técnica:**

1. **`FROM python:3.12-alpine3.17`**
   - Utiliza Python 3.12 con Alpine Linux

2. **`WORKDIR /app`**
   - Establece `/app` como directorio de trabajo dentro del contenedor
   - Todos los comandos posteriores se ejecutan desde aquí

3. **`COPY requirements.txt` + `RUN pip install`**
   - Estrategia de capas de Docker: Copia dependencias primero
   - Si `requirements.txt` no cambia, Docker usa caché
   - Acelera builds subsecuentes significativamente

4. **`CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]`**
   - `--host=0.0.0.0`: Expone Flask en todas las interfaces de red

---

### 3. Dockerfile - Frontend

**Ubicación:** `frontend/Dockerfile`

```dockerfile
FROM nginx:latest

# Path: /usr/share/nginx/html
COPY /sitio /usr/share/nginx/html
```

**Explicación técnica:**

1. **`FROM nginx:latest`**
   - Utiliza la imagen oficial de Nginx

2. **`COPY /sitio /usr/share/nginx/html`**
   - Copia todos los archivos estáticos al directorio web de Nginx
   - `/usr/share/nginx/html` es el directorio por defecto donde Nginx sirve archivos

---

### 4. Docker Compose

**Ubicación:** `docker-compose.yml`

```yaml
version: '3.8'

services:
  # ==================== SERVICIO: BASE DE DATOS ====================
  database:
    image: database
    build:
      context: ./database
      dockerfile: Dockerfile
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: linktree_db
      MYSQL_USER: user
      MYSQL_PASSWORD: userpassword
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

  # ==================== SERVICIO: BACKEND API ====================
  backend:
    image: backend
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      DB_HOST: database
      DB_USER: user
      DB_PASSWORD: userpassword
      DB_NAME: linktree_db
    depends_on:
      - database

  # ==================== SERVICIO: FRONTEND WEB ====================
  frontend:
    image: frontend
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "8080:80"
    depends_on:
      - backend

volumes:
  mysql_data:
```

**Características clave:**

1. **Networking automático:**
   - Docker Compose crea una red `front-back-bd_default`
   - DNS interno: Los servicios se comunican por nombre

2. **Orden de inicio con `depends_on`:**
   - `frontend` espera a `backend`
   - `backend` espera a `database`

3. **Persistencia de datos:**
   - Volumen `mysql_data` sobrevive a recreación de contenedores

---

## 🌐 Endpoints de la API

### GET `/getMyInfo`

Obtiene la información del usuario desde la base de datos.

**Request:**
```http
GET http://localhost:5000/getMyInfo
Content-Type: application/json
```

**Response (200 OK):**
```json
{
  "name": "Frida",
  "lastname": "Kahlo",
  "socialMedia": {
    "facebookUser": "fridaKahlo10",
    "instagramUser": "fridaKahlo10",
    "xUser": "kahloFrida",
    "linkedin": "fridaKahlo10",
    "githubUser": "kahloFridaGit"
  },
  "blog": "https://fridakahlo.com",
  "author": "Frida Kahlo"
}
```

---

## 🧪 Pruebas y Verificación

### 1. Verificar Contenedores Activos

```bash
docker-compose ps
```

### 2. Verificar Logs

```bash
# Logs de todos los servicios
docker-compose logs

# Logs en tiempo real
docker-compose logs -f

# Logs de un servicio específico
docker-compose logs backend
```

### 3. Probar Base de Datos

```bash
docker exec -it database mysql -u user -puserpassword linktree_db
```

### 4. Probar Backend API

```bash
curl -X GET http://localhost:5000/getMyInfo
```

### 5. Probar Frontend

Abrir navegador en: `http://localhost:8080/linktree.html`

---

## 📋 Comandos Útiles

### Gestión de Contenedores

```bash
# Iniciar servicios
docker-compose up
docker-compose up -d
docker-compose up --build

# Detener servicios
docker-compose stop
docker-compose down
docker-compose down -v

# Reiniciar servicios
docker-compose restart
docker-compose restart backend
```

### Inspección

```bash
# Ver logs
docker-compose logs -f

# Ejecutar comandos
docker exec -it database bash

# Ver recursos
docker stats
```
---

## 👥 Autores

**Proyecto desarrollado para:**
- 🎓 Actividad: EA2 - Contenerización de una Aplicación Web
- 📚 Curso: Tecnologías Web
- 🏫 Institución Universitaria Digital de Antioquia (IUD)
- 📅 Fecha: Diciembre 2025

**Repositorio:** [https://github.com/1531nana/app-contenerizar-TW](https://github.com/1531nana/app-contenerizar-TW)

---
