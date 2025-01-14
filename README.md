# Cuisine and Visitor Management API

This project provides APIs to manage cuisines, visitors, visits, and visitor status.



## Installation and Setup

### Prerequisites

- Python 3.9+
- Django 5.1
- Django REST Framework
- PostgreSQL (optional, for production environments)

### Steps

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. **Install Dependencies**
   Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate 
   pip install -r requirements.txt
   ```

3. **Set Up the Database**
   Update `DATABASES` in `settings.py` for your database configuration.
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the API**
   Navigate to `http://127.0.0.1:8000/api/` in your browser or API client.

---

## API Endpoints

### User Endpoints
Login           /GET /  http://localhost:8000/api/auth/jwt/create
User profile    /GET /  http://localhost:8000/api/auth/users/me/
User register   /POST / http://localhost:8000/api/auth/users/
User activation /POST / http://localhost:8000/api/auth/users/activation/
User delete     /DELETE /http://localhost:8000/api/auth/users/me/
User update     /PATCH / http://localhost:8000/api/auth/users/me/
User set new password / POST / http://localhost:8000/api/auth/users/set_password/
User reset password  /POST / http://localhost:8000/api/auth/users/reset_password/
User reset password confirmation /POST / http://localhost:8000/api/auth/users/set_password/
 
### Resturant Endpoints
Restaurant list / GET /http://localhost:8000/api/diary/restaurants/
Restaurant single-create /POST / http://localhost:8000/api/diary/restaurants/
Resturant single-get /GET /http://localhost:8000/api/diary/restaurants/1/
Restaurant single-update /PATCH / http://localhost:8000/api/diary/restaurants/1/
Restaurant single-delete /DELETE / http://localhost:8000/api/diary/restaurants/1/
Resturant reviews-list/GET /http://localhost:8000/api/diary/restaurants/1/reviews
Resturant photos /GET / http://localhost:8000/api/diary/restaurants/1/photos


### Cuisine Endpoints
Cuisine list / GET /http://localhost:8000/api/diary/cuisines/
Cuisine signe-create / POST/ http://localhost:8000/api/diary/cuisines/
Cuisine single-get /GET / http://localhost:8000/api/diary/cuisines/1/
Cuisine single-update /GET / http://localhost:8000/api/diary/cuisines/1/
Cuisine single photos /GET / http://localhost:8000/api/diary/cuisines/1/photos


### Visits Endpoints
Visits list /GET / http://localhost:8000/api/diary/visits/
Visits single-create /POST /  http://localhost:8000/api/diary/visits/
Visits single-get /GET / http://localhost:8000/api/diary/visits/1/
Visites single-update /PATCH / http://localhost:8000/api/diary/visits/1/
Visits single-delete /DELETE / http://localhost:8000/api/diary/visits/1/


---
## Testing
python manage.py test

---
## License

This version is designed to be clean, concise, and easy to follow for developers who need to quickly get up to speed with your project.
