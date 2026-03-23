# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Initial Setup (One-time)

1. Open Command Prompt/PowerShell in the project directory
2. Run the setup script:
   ```bash
   setup.bat
   ```
   This will:
   - Create virtual environment
   - Install all dependencies
   - Train the ML model
   - Setup the database

   **Wait for completion** - The ML model training might take 1-2 minutes.

### Step 2: Start Django Backend

1. Open a **NEW** Command Prompt/PowerShell
2. Navigate to the project folder
3. Run:
   ```bash
   run-django.bat
   ```
4. Wait for: `Starting development server at http://127.0.0.1:8000/`

### Step 3: Start Streamlit Frontend

1. Open another **NEW** Command Prompt/PowerShell
2. Navigate to the project folder
3. Run:
   ```bash
   run-streamlit.bat
   ```
4. The app should automatically open at `http://localhost:8501`

## 📝 First Use

### Create an Account
1. Click **Register** button
2. Fill in:
   - First Name
   - Last Name
   - Username (unique)
   - Email
   - Password (min 8 chars)
   - Confirm Password
3. Click **Register**

### Make Your First Prediction
1. After login, click **Predictor**
2. Fill in customer information:
   - Age: 35-65 typical
   - Annual Income: 30,000-200,000
   - Credit Score: 300-850
   - Credit Utilization: 0-100%
   - Missed Payments: 0-10
   - Loan Balance: Any amount
   - Debt-to-Income: 0-100%
   - Account Tenure: 0-40 years
   - Employment Status: Select from dropdown
   - Credit Card Type: Select from dropdown
   - Location: Urban/Suburban/Rural
3. Click **Make Prediction**
4. View results with risk level and probability

### View Your History
1. Click **History**
2. See all past predictions
3. Expand each prediction for details

## 🔧 Troubleshooting

### Issue: "Connection refused" error
**Solution**: Make sure Django backend is running first before starting Streamlit

### Issue: "Model not found" error
**Solution**: The ML model wasn't trained. Run:
```bash
cd credit_app\ml_model
python train_model.py
```

### Issue: Port already in use
**Solution**: Kill the process using the port or use a different port:
```bash
# For Django on different port
python manage.py runserver 8001

# For Streamlit on different port (modify streamlit config)
```

### Issue: Dependencies not working
**Solution**: Reinstall dependencies:
```bash
venv\Scripts\activate.bat
pip install --upgrade -r requirements.txt
```

## 📊 Sample Test Data

Try these values for testing:

### Low Risk Customer
- Age: 45
- Income: $120,000
- Credit Score: 750
- Credit Utilization: 10%
- Missed Payments: 0
- Loan Balance: $15,000
- Debt-to-Income: 15%
- Tenure: 10 years

### Medium Risk Customer
- Age: 35
- Income: $60,000
- Credit Score: 650
- Credit Utilization: 50%
- Missed Payments: 2
- Loan Balance: $25,000
- Debt-to-Income: 45%
- Tenure: 5 years

### High Risk Customer
- Age: 30
- Income: $40,000
- Credit Score: 550
- Credit Utilization: 90%
- Missed Payments: 5
- Loan Balance: $30,000
- Debt-to-Income: 75%
- Tenure: 2 years

## 📱 Features Summary

| Feature | Details |
|---------|---------|
| **User Auth** | Secure register/login |
| **Predictions** | Real-time ML predictions |
| **History** | Track all predictions |
| **Risk Levels** | Low/Medium/High classification |
| **Probability** | Delinquency probability % |
| **Mobile Ready** | Works on mobile browsers |
| **Secure** | Encrypted & validated data |

## 🔐 Admin Panel

Access Django Admin:
1. Navigate to: http://localhost:8000/admin
2. Create superuser (if not done):
   ```bash
   cd credit_app/creditproject
   python manage.py createsuperuser
   ```
3. Login with admin credentials
4. Manage users and view predictions

## 📞 Need Help?

Check these in order:
1. Terminal for error messages
2. README.md for detailed information
3. Browser console (F12) for frontend errors
4. Django console output for backend errors

## ✅ Verification Checklist

- [ ] setup.bat ran successfully
- [ ] run-django.bat shows "Starting development server"
- [ ] run-streamlit.bat shows "You can now view your Streamlit app"
- [ ] Browser opens to http://localhost:8501
- [ ] Can register a new account
- [ ] Can login successfully
- [ ] Can make a prediction
- [ ] Prediction result appears with risk level

Once all checkboxes are checked, your app is ready to use!

---

**Happy Predicting! 🎉**
