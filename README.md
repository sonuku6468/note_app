# note_app
A simple note-taking RESTful API built with Django and Django REST Framework.

## Setup

1. Clone the repository:
    ```
    git clone <https://github.com/sonuku6468/note_app.git>
    cd notes_project
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Run the server:
    ```
    python manage.py runserver
    ```

5. Access the Swagger UI for API documentation:
    ```
    http://127.0.0.1:8000/swagger/
    ```

## Endpoints

- **Create Note:** `POST /api/notes/`
- **Fetch Note by ID:** `GET /api/notes/<pk>/`
- **Query Notes by Title Substring:** `GET /api/notes/search/?title=<substring>`
- **Update Note:** `PUT /api/notes/update/<pk>/`

## Testing

Run the following command to execute tests:'python manage.py test'
