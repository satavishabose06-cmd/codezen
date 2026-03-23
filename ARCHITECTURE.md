# System Architecture

## Overview

The Credit Delinquency Prediction App is a three-tier architecture consisting of:

1. **Machine Learning Model** - ML Model Training & Prediction
2. **Backend API** - Django REST Framework (Authentication & Predictions)
3. **Frontend UI** - Streamlit (User Interface)

```
┌─────────────────────────────────────────────────────────────┐
│                    USER BROWSER                              │
│                  (http://localhost:8501)                     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ HTTP/WebSocket
                         ▼
┌──────────────────────────────────────────────────────────────┐
│              STREAMLIT FRONTEND (app.py)                      │
│  ─────────────────────────────────────────────────────────   │
│  • Home Page - Welcome & About                               │
│  • User Authentication Pages                                 │
│  • Prediction Interface                                      │
│  • Prediction History                                        │
│  • User Profile                                              │
│  • Navigation Bar                                            │
└────────────────────────┬───────────────────────────────────┘
                         │
                         │ REST API Calls
                         │ (http://localhost:8000/api)
                         ▼
┌──────────────────────────────────────────────────────────────┐
│         DJANGO BACKEND (creditproject)                       │
│  ─────────────────────────────────────────────────────────   │
│                                                              │
│  ┌─────────────────────┐      ┌──────────────────────────┐ │
│  │  Users App          │      │  Predictor App          │ │
│  │  ─────────────────  │      │  ───────────────────    │ │
│  │  • Register         │      │  • Make Prediction      │ │
│  │  • Login            │      │  • Get History          │ │
│  │  • Logout           │      │  • Store Results        │ │
│  │  • Profile          │      │  • Load ML Model        │ │
│  │  • Token Auth       │      │                         │ │
│  └─────────────────────┘      └──────────────────────────┘ │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │            SQLite Database (db.sqlite3)              │   │
│  │  ──────────────────────────────────────────────────  │   │
│  │  • Users Table                                       │   │
│  │  • Auth Tokens                                       │   │
│  │  • Prediction History                               │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
└────────────────────────┬───────────────────────────────────┘
                         │
                         │ Load Model
                         │ (Joblib)
                         ▼
┌──────────────────────────────────────────────────────────────┐
│          ML MODEL (credit_app/ml_model)                      │
│  ─────────────────────────────────────────────────────────   │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ model.pkl    │  │ scaler.pkl   │  │encoders.pkl  │      │
│  │              │  │              │  │              │      │
│  │ Random Forest│  │ Standard     │  │ Label        │      │
│  │ Classifier   │  │ Scaler       │  │ Encoders     │      │
│  │              │  │              │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                              │
│  Trained on: Delinquency_prediction_dataset.xlsx            │
│  • 500 records                                              │
│  • 19 features                                              │
│  • Binary classification (Delinquent/Not Delinquent)       │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Frontend (Streamlit)

**File**: `streamlit_app/app.py`

**Pages**:
- **Home**: Welcome screen with features overview
- **Register**: New user registration
- **Login**: User authentication
- **Predictor**: Main prediction interface
- **History**: View past predictions
- **Profile**: User account information

**Features**:
- Session management
- Token-based API communication
- Real-time form validation
- Responsive design
- Professional styling

### 2. Backend (Django)

**Structure**:
```
credit_app/creditproject/
├── creditproject/          # Project settings
│   ├── settings.py        # Django configuration
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI application
├── users/                 # Authentication app
│   ├── models.py          # User models
│   ├── views.py           # Authentication views
│   ├── serializers.py     # DRF serializers
│   ├── urls.py            # App URLs
│   └── signals.py         # Token creation signals
├── predictor/             # Prediction app
│   ├── models.py          # Prediction history model
│   ├── views.py           # Prediction API views
│   ├── serializers.py     # Input/Output serializers
│   ├── urls.py            # App URLs
│   └── prediction_model.py # ML model interface
└── manage.py              # Django CLI
```

**Endpoints**:

| Method | Endpoint | Auth | Purpose |
|--------|----------|------|---------|
| POST | /api/users/register/ | No | Register user |
| POST | /api/users/login/ | No | Login & get token |
| POST | /api/users/logout/ | Yes | Logout user |
| GET | /api/users/profile/ | Yes | Get user info |
| POST | /api/predictor/predict/ | Yes | Make prediction |
| GET | /api/predictor/history/ | Yes | Get prediction history |

### 3. Machine Learning

**File**: `credit_app/ml_model/train_model.py`

**Pipeline**:

```
1. Data Loading
   └─ Read Excel file
   
2. Data Preprocessing
   ├─ Handle missing values
   ├─ Encode categorical features
   └─ Map payment status
   
3. Feature Engineering
   ├─ Separate features & target
   ├─ Train-test split
   ├─ Feature scaling
   └─ Prepare dataset
   
4. Model Training
   ├─ Random Forest (100 estimators)
   ├─ Hyperparameter tuning
   └─ Cross-validation
   
5. Model Evaluation
   ├─ Accuracy calculation
   ├─ ROC-AUC score
   ├─ Classification report
   └─ Confusion matrix
   
6. Model Serialization
   ├─ Save model.pkl
   ├─ Save scaler.pkl
   ├─ Save encoders.pkl
   └─ Save feature_names.pkl
```

**Model Configuration**:
- Algorithm: Random Forest Classifier
- Estimators: 100
- Max Depth: 15
- Min Samples Split: 5
- Random State: 42

## Database Schema

### Users Table (Built-in Django)
```sql
CREATE TABLE auth_user (
    id INTEGER PRIMARY KEY,
    username VARCHAR(150) UNIQUE,
    email VARCHAR(254),
    password VARCHAR(128),
    first_name VARCHAR(150),
    last_name VARCHAR(150),
    is_staff BOOLEAN,
    is_active BOOLEAN,
    date_joined DATETIME
);
```

### Authentication Tokens Table
```sql
CREATE TABLE authtoken_token (
    key VARCHAR(40) PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES auth_user(id),
    created DATETIME
);
```

### Prediction History Table
```sql
CREATE TABLE predictor_predictionhistory (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES auth_user(id),
    age INTEGER,
    income FLOAT,
    credit_score FLOAT,
    credit_utilization FLOAT,
    missed_payments INTEGER,
    loan_balance FLOAT,
    debt_to_income_ratio FLOAT,
    employment_status VARCHAR(50),
    account_tenure INTEGER,
    credit_card_type VARCHAR(50),
    location VARCHAR(100),
    prediction INTEGER,
    probability FLOAT,
    created_at DATETIME
);
```

## Data Flow

### Registration Flow
```
User → Fills Form → Streamlit
  ↓
Streamlit → POST /api/users/register/ → Django
  ↓
Django → Validates Data, Hashes Password → Database
  ↓
Response + Token → Streamlit
  ↓
Store Token in Session → User Logged In
```

### Prediction Flow
```
User → Fills Prediction Form → Streamlit
  ↓
Streamlit → POST /api/predictor/predict/ + Token → Django
  ↓
Django → Receives Request, Validates Data
  ↓
Load ML Model → Preprocess Features → Make Prediction
  ↓
Return Prediction + Probability → Save to Database
  ↓
Response → Streamlit → Display Results
  ↓
Store Prediction in History → User sees in History tab
```

## Authentication Flow

```
1. Register
   ├─ Username + Password → Server
   ├─ Hash Password
   ├─ Create User
   ├─ Generate Token
   └─ Return Token

2. Login
   ├─ Username + Password → Server
   ├─ Verify Credentials
   ├─ Generate/Get Token
   └─ Return Token

3. API Request (with Token)
   ├─ Authorization: Token <token>
   ├─ Server validates token
   ├─ Process request
   └─ Return response

4. Logout
   ├─ Delete Token
   ├─ Clear Session
   └─ Redirect to Home
```

## Security Architecture

```
┌──────────────────────────────────────────┐
│         Security Layers                  │
├──────────────────────────────────────────┤
│ 1. HTTPS/TLS                             │ (In production)
│ 2. CORS Validation                       │
│ 3. CSRF Protection                       │
│ 4. Authentication (Token)                │
│ 5. Authorization (Permissions)           │
│ 6. Input Validation                      │
│ 7. SQL Injection Prevention               │
│ 8. Password Hashing (PBKDF2)             │
│ 9. Rate Limiting                         │ (Optional)
│ 10. Logging & Monitoring                 │
└──────────────────────────────────────────┘
```

## Deployment Architecture (Production)

```
                    ┌──────────────────┐
                    │   Load Balancer  │
                    └────────┬─────────┘
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
    ┌────────┐          ┌────────┐          ┌────────┐
    │Django #1│         │Django #2│         │Django #3│
    │(Port 80)│         │(Port 81)│         │(Port 82)│
    └────┬───┘          └────┬───┘          └────┬───┘
         │                   │                   │
         └───────────────────┼───────────────────┘
                             │
                    ┌────────▼────────┐
                    │PostgreSQL       │
                    │(Production DB)  │
                    └─────────────────┘

    Streamlit (with Nginx reverse proxy)
                             │
                    ┌────────▼────────┐
                    │Redis Cache      │
                    └─────────────────┘
```

## Technology Stack Summary

| Component | Technology | Version |
|-----------|-----------|---------|
| Frontend | Streamlit | 1.28.0 |
| Backend | Django | 4.2.0 |
| API | Django REST Framework | 3.14.0 |
| Database | SQLite (Dev)/PostgreSQL (Prod) | - |
| ML | Scikit-learn | 1.3.0 |
| Data | Pandas, NumPy | 2.0.0, 1.24.0 |
| Python | Python | 3.8+ |

## Performance Considerations

- **ML Model Loading**: Model loaded into memory on first request (≈50MB)
- **Prediction Speed**: <100ms per prediction
- **API Response Time**: <200ms average
- **Database**: SQLite fine for dev, PostgreSQL for production
- **Caching**: Can implement Redis for predictions cache

---

**Document Version**: 1.0  
**Last Updated**: March 2024
