@echo off
REM Run Streamlit Frontend
echo.
echo ================================================
echo STREAMLIT FRONTEND
echo ================================================
echo.
echo App URL: http://localhost:8501
echo.
echo Make sure Django backend is running!
echo Press Ctrl+C to stop the server
echo.

call venv\Scripts\activate.bat
cd streamlit_app
streamlit run app.py
