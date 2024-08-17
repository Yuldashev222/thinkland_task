# Task by "Thinkland"

### 1. Clone the Repository

```bash
git clone https://github.com/Yuldashev222/thinkland_task.git
```

### 2. Change Directory

```bash
cd thinkland_task 
```

### 3. Create .env file using .env.example

```bash
mv .env.example .env
```

### 4. Run project

```bash
docker-compose up --build
```

### 5. Create Elasticsearch Index and generate fake data (in other CMD)

```bash
docker-compose exec django_app ./manage.py generate_data 
```

### 6. create superuser for admin panel (Optional) (in other CMD)

```bash
docker-compose exec django_app ./manage.py createsuperuser 
```

### 7. Available APIs

#### API DOC (Swagger)

http://localhost:8000/

#### login API

http://localhost:8000/auth/login/

#### register API

http://localhost:8000/auth/register/

#### search using elasticsearch

http://localhost:8000/products/search/?q={search_query}

#### product list, create

http://localhost:8000/products/

#### product detail, update, delete

http://localhost:8000/products/{id}/

#### category list, create

http://localhost:8000/products/categories/

#### category detail, update, delete

http://localhost:8000/products/categories/{id}/

