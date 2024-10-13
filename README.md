# Rooms-API

**Rooms-api** is a RESTful API project created to utilise room booking accounting. The project is developed using **Django**, **Docker**, **Django REST Framework** and **PostgreSQL** as the database.

## 🚀 Quick Start

Follow these steps to get up and running with the Rooms-API on your local machine.

### 1. Clone the Repository

Start by cloning the repository:

```bash
git clone https://github.com/your-repo/Base-api.git
cd book-api
```

### 2. Create a virtual environment

```bash
python3 -m venv env
# Activate the environment (Linux/Mac)
source env/bin/activate
# Activate on Windows
env\Scripts\activate
```

### 3. Once activated, install the required dependencies listed in requirements.txt

```bash
pip install -r requirements.txt
```

### 3. Docker container launch

```bash
docker compose up -d --build
```

### 4. Database create migration

```bash
chmod +x <migrate.sh>
sudo ./migrate.sh
```

### 5. Create superuser admin

```bash
docker exec -it <id> shell
python3 manage.py createsuperuser
```
