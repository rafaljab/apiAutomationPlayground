@ECHO OFF
CD "%~dp0"
.\.venv\Scripts\activate && python manage.py runserver
EXIT
