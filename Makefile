migrate:
    python3 create_db.py
    python3 manage.py makemigrations
    python3 manage.py migrate
