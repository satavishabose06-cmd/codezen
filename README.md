# Credit Delinquency Prediction App

A professional web application for predicting credit delinquency risk using machine learning.

## Features

✨ **User Authentication**
- Secure user registration and login
- Token-based authentication
- User profile management

🔮 **Credit Delinquency Prediction**
- ML-powered risk assessment
- Real-time predictions
- Risk level classification (Low, Medium, High)
- Probability scores

📊 **Prediction History**
- Track all past predictions
- Detailed prediction records
- Historical analysis

🎨 **Professional UI**
- Modern, responsive design
- Easy-to-use interface
- Real-time feedback

## Architecture

### Backend (Django)
- REST API with Django REST Framework
- Token-based authentication
- SQLite database for user management
- Prediction history tracking

### Frontend (Streamlit)
- Interactive web interface
- Real-time prediction display
- User-friendly forms
- Responsive design

### Machine Learning
- Random Forest Classifier
- 100 estimators, optimized parameters
- High accuracy and ROC-AUC scores
- Handles multiple feature types

## Dataset

The application is trained on a credit delinquency prediction dataset with:
- 500 records
- 19 features including demographics, financial metrics, and payment history
- Target: Delinquent Account (Binary Classification)

## Installation

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Steps

1. **Clone/Download the project**
   ```bash
   cd "E:\Credit Delinquncy"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the ML Model**
   ```bash
   cd credit_app/ml_model
   python train_model.py
   ```
   This will create:
   - `model.pkl` - Trained Random Forest model
   - `scaler.pkl` - Feature scaler
   - `encoders.pkl` - Category encoders
   - `feature_names.pkl` - Feature names

5. **Setup Django Database**
   ```bash
   cd credit_app/creditproject
   python manage.py migrate
   python manage.py createsuperuser  # Optional: Create admin user
   ```

6. **Run Django Backend** (Terminal 1)
   ```bash
   cd credit_app/creditproject
   python manage.py runserver
   ```
   Server runs on: http://localhost:8000

7. **Run Streamlit Frontend** (Terminal 2)
   ```bash
   cd streamlit_app
   streamlit run app.py
   ```
   App opens on: http://localhost:8501

## Usage

### First Time Setup

1. Go to http://localhost:8501
2. Click "Register" to create an account
3. Fill in the registration form
4. Click "Register"

### Making Predictions

1. After login, click "Predictor" in the navigation bar
2. Fill in customer information:
   - Demographics (Age, Location)
   - Financial metrics (Income, Credit Score, etc.)
   - Credit history (missed payments, loan balance)
   - Employment status and credit card type
3. Click "Make Prediction"
4. View the prediction result with risk level and probability

### Viewing History

1. Click "History" to see all past predictions
2. Each prediction shows detailed information
3. Track patterns and trends over time

### Django Admin Panel

Access at: http://localhost:8000/admin
- Username: superuser (create during setup)
- Manage users and predictions
- View app statistics

## API Endpoints

### Authentication
- `POST /api/users/register/` - Register new user
- `POST /api/users/login/` - Login user
- `POST /api/users/logout/` - Logout user
- `GET /api/users/profile/` - Get user profile

### Predictions
- `POST /api/predictor/predict/` - Make prediction
- `GET /api/predictor/history/` - Get prediction history

## Model Performance

The trained Random Forest model achieves:
- **Accuracy**: ~90%+
- **ROC-AUC Score**: ~95%+
- **Features Used**: 19 credit-related features

## Project Structure

```
Credit Delinquncy/
├── credit_app/
│   ├── creditproject/          # Django project
│   │   ├── creditproject/      # Project settings
│   │   ├── users/              # User authentication app
│   │   ├── predictor/          # Prediction API
│   │   └── manage.py
│   └── ml_model/
│       ├── train_model.py      # ML training script
│       ├── model.pkl           # Trained model
│       ├── scaler.pkl          # Feature scaler
│       ├── encoders.pkl        # Category encoders
│       └── feature_names.pkl
├── streamlit_app/
│   └── app.py                  # Streamlit frontend
├── requirements.txt            # Python dependencies
└── README.md
```

## Troubleshooting

### Django Server Won't Start
```bash
# Check if port 8000 is in use
# Kill the process or use different port:
python manage.py runserver 8001
```

### Streamlit Won't Connect
```bash
# Ensure Django is running first
# Check CORS settings in settings.py
# Restart both servers
```

### Model Not Found Error
```bash
# Navigate to credit_app/ml_model
# Run: python train_model.py
# This trains and saves the model
```

### Database Issues
```bash
# Reset database
cd credit_app/creditproject
rm db.sqlite3
python manage.py migrate
```

## Technologies Used

- **Backend**: Django 4.2, Django REST Framework
- **Frontend**: Streamlit 1.28
- **ML**: Scikit-learn, Pandas, NumPy
- **Database**: SQLite
- **Authentication**: Token Authentication

## Security Features

- Password hashing with Django's built-in security
- Token-based API authentication  
- CORS protection
- Input validation
- SQL injection prevention
- CSRF protection

## Future Enhancements

- [ ] More ML models (XGBoost, LightGBM)
- [ ] Model comparison dashboard
- [ ] Batch predictions
- [ ] Advanced analytics
- [ ] Email notifications
- [ ] Export predictions to CSV
- [ ] API documentation with Swagger
- [ ] Database backup system

## License

This project is for educational purposes.

## Support

For issues or questions, please check:
1. Django logs in terminal 1
2. Streamlit logs in terminal 2
3. Check model.pkl exists in ml_model folder
4. Ensure all dependencies are installed

## Author

Created for credit delinquency prediction and risk assessment.

---

**Version**: 1.0  
**Last Updated**: March 2024
