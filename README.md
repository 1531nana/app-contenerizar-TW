# Aplicación Web Contenerizada - Linktree Full-Stack

## 📋 Descripción del Proyecto

Aplicación web full-stack tipo Linktree que muestra información de perfil y enlaces a redes sociales. La aplicación está completamente contenerizada usando Docker y Docker Compose, incluyendo:

- **Frontend**: Interfaz web estática servida por Nginx
- **Backend**: API REST desarrollada en Python con Flask
- **Base de Datos**: MySQL 8.0 para almacenamiento persistente

## 🏗️ Arquitectura

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│  Frontend   │─────▶│   Backend   │─────▶│   MySQL     │
│  (Nginx)    │      │   (Flask)   │      │  Database   │
│  Port: 8080 │      │  Port: 5000 │      │  Port: 3306 │
└─────────────┘      └─────────────┘      └─────────────┘
```

## 🛠️ Tecnologías Utilizadas

### Frontend
- HTML5, CSS3, JavaScript
- Nginx (servidor web)
- Framework CSS: W3.CSS
- Iconos: Feather Icons

### Backend
- Python 3.12
- Flask 3.0.0
- Flask-CORS
- mysql-connector-python

### Base de Datos
- MySQL 8.0
- Persistencia con Docker Volumes

### DevOps
- Docker
- Docker Compose 3.8

## 🚀 Instalación y Despliegue

### Pasos para Ejecutar

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/1531nana/app-contenerizar-TW
   cd front-back-bd
   ```

2. **Construir y levantar los contenedores**
   ```bash
   docker-compose up --build
   ```

   Este comando:
   - Construye las imágenes de frontend y backend
   - Descarga la imagen de MySQL
   - Crea y configura la red de Docker
   - Inicia los tres servicios en el orden correcto
   - Ejecuta el script de inicialización de la base de datos

3. **Verificar que los servicios estén corriendo**
   ```bash
   docker-compose ps
   ```

4. **Acceder a la aplicación**
   - Frontend: http://localhost:8080/linktree.html
   - Backend API: http://localhost:5000/getMyInfo
   - MySQL: localhost:3306

## 🔧 Configuración Detallada

### Docker Compose (docker-compose.yml)

El archivo `docker-compose.yml` orquesta tres servicios:

#### Servicio: Base de Datos (db)
```yaml
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
```

**Características:**
- Se construye desde el Dockerfile local
- Crea automáticamente la base de datos `linktree_db`
- Volumen persistente para los datos

#### Servicio: Backend (backend)
```yaml
backend:
    image: backend
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - 5000:5000
    environment:
      DB_HOST: database
      DB_USER: user
      DB_PASSWORD: userpassword
      DB_NAME: linktree_db
    depends_on:
      - database
```

**Características:**
- Se construye desde el Dockerfile local
- Variables de entorno para conexión a BD
- Espera a que MySQL esté saludable antes de iniciar
- Expone API REST en puerto 5000

#### Servicio: Frontend (frontend)
```yaml
frontend:
    image: frontend
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - 8080:80
    depends_on:
      - backend
```

**Características:**
- Servidor Nginx con archivos estáticos
- Depende del backend
- Accesible en puerto 8080

## 🧪 Pruebas

### Probar el Backend directamente
```bash
curl http://localhost:5000/getMyInfo
```

### Probar la Base de Datos
```bash
docker exec -it mysql_db mysql -u user -puserpassword linktree_db -e "SELECT * FROM user_info;"
```

### Verificar logs
```bash
# Backend
docker-compose logs backend

# Base de datos
docker-compose logs db
```

## 👥 Autor

Proyecto desarrollado para la actividad EA2 - Contenerización de Aplicaciones Web

