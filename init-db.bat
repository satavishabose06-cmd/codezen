@echo off
REM Django Database Initialization
echo.
echo ================================================
echo Django Database Initialization
echo ================================================
echo.

call venv\Scripts\activate.bat
cd credit_app\creditproject

echo [1] Running migrations...
python manage.py migrate

echo.
echo [2] Creating superuser for admin...
echo Password should be at least 8 characters
python manage.py createsuperuser

echo.
echo ================================================
echo Database initialization complete!
echo ================================================
echo.
echo You can now login to admin at:
echo http://localhost:8000/admin
echo.
pause
