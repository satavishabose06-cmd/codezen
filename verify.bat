@echo off
REM Verification and Troubleshooting Script
echo.
echo ================================================
echo Credit App - Verification & Troubleshooting
echo ================================================
echo.

SET passed=0
SET total=0

REM Check 1: Python Installation
SET /A total+=1
echo [Check 1] Verifying Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ FAILED: Python not installed or not in PATH
    echo SOLUTION: Install Python 3.8+ and add to PATH
) else (
    for /f "tokens=*" %%i in ('python --version 2^>^&1') do set version=%%i
    echo ✓ PASSED: %version%
    SET /A passed+=1
)
echo.

REM Check 2: Virtual Environment
SET /A total+=1
echo [Check 2] Checking virtual environment...
if exist venv\Scripts\activate.bat (
    echo ✓ PASSED: Virtual environment exists
    SET /A passed+=1
) else (
    echo ❌ FAILED: Virtual environment not found
    echo SOLUTION: Run setup.bat first
)
echo.

REM Check 3: Dependencies
SET /A total+=1
echo [Check 3] Checking dependencies...
call venv\Scripts\activate.bat >nul 2>&1
pip show django >nul 2>&1
if errorlevel 1 (
    echo ❌ FAILED: Dependencies not installed
    echo SOLUTION: Run: pip install -r requirements.txt
) else (
    echo ✓ PASSED: Django and dependencies installed
    SET /A passed+=1
)
echo.

REM Check 4: ML Model
SET /A total+=1
echo [Check 4] Checking ML model files...
if exist credit_app\ml_model\model.pkl (
    echo ✓ PASSED: model.pkl found
    SET /A passed+=1
) else (
    echo ❌ FAILED: model.pkl not found
    echo SOLUTION: Run: cd credit_app\ml_model ^&^& python train_model.py
)
echo.

REM Check 5: Django Settings
SET /A total+=1
echo [Check 5] Checking Django setup...
if exist credit_app\creditproject\creditproject\settings.py (
    echo ✓ PASSED: Django settings exist
    SET /A passed+=1
) else (
    echo ❌ FAILED: Django settings not found
    echo SOLUTION: Reinstall project files
)
echo.

REM Check 6: Streamlit App
SET /A total+=1
echo [Check 6] Checking Streamlit app...
if exist streamlit_app\app.py (
    echo ✓ PASSED: Streamlit app exists
    SET /A passed+=1
) else (
    echo ❌ FAILED: Streamlit app not found
    echo SOLUTION: Reinstall project files
)
echo.

REM Check 7: Dataset
SET /A total+=1
echo [Check 7] Checking dataset file...
if exist "d:\3RD SEM NOTES\Delinquency_prediction_dataset.xlsx" (
    echo ✓ PASSED: Dataset found
    SET /A passed+=1
) else (
    echo ⚠ WARNING: Dataset not found at expected location
    echo NOTE: This is only needed for retraining the model
)
echo.

REM Summary
echo ================================================
echo Verification Summary
echo ================================================
echo Checks Passed: %passed%/%total%
echo.

if %passed% equ %total% (
    echo ✓ ALL CHECKS PASSED!
    echo.
    echo Your app is ready to run:
    echo.
    echo 1. Open Terminal 1: run-django.bat
    echo 2. Open Terminal 2: run-streamlit.bat
    echo 3. Go to http://localhost:8501
    echo.
) else (
    echo ❌ SOME CHECKS FAILED
    echo.
    echo Please fix the issues shown above
    echo Run setup.bat to reinitialize if needed
    echo.
)

pause
