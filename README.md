# Cuisine and Visitor Management API

This project provides APIs to manage cuisines, visitors, visits, and visitor status.

## Features

- Manage cuisines and their photos.
- Create, read, update, and delete cuisines.
- Record visitor visits, expenses, and ratings.
- Retrieve visitor status, including total visits, total expenses, and ordered cuisines.

---

## Installation and Setup

### Prerequisites

- Python 3.8+
- Django 3.2+
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
   source venv/bin/activate  # On Windows: venv\Scripts\activate
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

### Cuisine Endpoints

| **Action**                     | **Method** | **Endpoint**           |
|--------------------------------|------------|------------------------|
| List/Create Cuisines           | `GET/POST` | `/api/cuisines/`       |
| Retrieve/Update/Delete Cuisine | `GET/PUT/DELETE` | `/api/cuisines/<id>/` |

### Visitor Endpoints

| **Action**            | **Method** | **Endpoint**   |
|-----------------------|------------|----------------|
| Get Visitor Profile   | `GET`      | `/api/profile/`|
| List/Create Visits    | `GET/POST` | `/api/visits/` |
| Visitor Statistics    | `GET`      | `/api/stats/`  |

---

## Models Overview

### Cuisine
- **Fields:**
  - `name`: Name of the cuisine.
  - `price`: Price of the cuisine.
  - `views`: Number of views (default: 0).

### CuisinePhoto
- **Fields:**
  - `cuisine`: Foreign key to Cuisine.
  - `photo`: Image file for the cuisine.

### VisitorProfile
- **Fields:**
  - `user`: Linked to the authenticated user.
  - `name`, `place`, `contact_info`, `email`: Visitor details.
  - `preferred_cuisine`: FK to `Cuisine`.

### Visit
- **Fields:**
  - `visitor`: Linked to `VisitorProfile`.
  - `cuisine`: FK to `Cuisine`.
  - `expense`, `comment`, `rating`, `visit_date`: Details of the visit.

---

## Example Requests

### Create a Cuisine
```json
POST /api/cuisines/
{
    "name": "Sushi",
    "price": "12.99"
}
```

### Retrieve Visitor Statistics
```json
GET /api/stats/
```
**Response:**
```json
{
    "total_visits": 5,
    "total_expenses": "125.50",
    "cuisines_ordered": ["Sushi", "Pizza"]
}
```

---

## Testing

Run tests using:
```bash
python manage.py test
```

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
