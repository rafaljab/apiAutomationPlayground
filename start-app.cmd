@ECHO OFF
CD "%~dp0"
uv run manage.py runserver
EXIT
