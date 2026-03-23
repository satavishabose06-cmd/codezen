@echo off
REM Credit Delinquency Prediction App - Setup Script
echo.
echo ================================================
echo Credit Delinquency Prediction App - Setup
echo ================================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo [1/4] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo.
echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/4] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [4/4] Training ML Model...
cd credit_app\ml_model
python train_model.py
if errorlevel 1 (
    echo WARNING: ML Model training had issues
    cd ..\..\
    pause
    exit /b 1
)

cd ..\..\

echo.
echo ================================================
echo Setup Complete!
echo ================================================
echo.
echo Next Steps:
echo 1. Run "run-django.bat" in Terminal 1
echo 2. Run "run-streamlit.bat" in Terminal 2
echo.
echo Then open your browser to http://localhost:8501
echo.
pause
