@echo off
REM Run Django Backend Server
echo.
echo ================================================
echo DJANGO BACKEND SERVER
echo ================================================
echo.
echo Server URL: http://localhost:8000
echo Admin URL: http://localhost:8000/admin
echo API URL: http://localhost:8000/api
echo.
echo Press Ctrl+C to stop the server
echo.

call venv\Scripts\activate.bat
cd credit_app\creditproject
python manage.py runserver
