# Project Structure & File Guide

## 📁 Complete Directory Structure

```
e:\Credit Delinquncy\
│
├── 📄 requirements.txt                 # Python dependencies
├── 📄 README.md                        # Complete documentation
├── 📄 QUICKSTART.md                    # Quick start guide (5 min setup)
├── 📄 COMPLETE_SETUP.md               # Comprehensive setup guide
├── 📄 ARCHITECTURE.md                  # System architecture & design
├── 📄 PROJECT_STRUCTURE.md            # This file
├── 📄 .gitignore                       # Git ignore rules
│
├── 🔧 setup.bat                        # MAIN: Run this first (one-time)
├── 🔧 run-django.bat                   # START: Django backend
├── 🔧 run-streamlit.bat                # START: Streamlit frontend
├── 🔧 verify.bat                       # CHECK: Verify installation
├── 🔧 init-db.bat                      # OPTIONAL: Initialize database
│
├── 📦 credit_app/                      # Django Backend
│   │
│   ├── creditproject/                  # Django Project Root
│   │   ├── 📄 manage.py               # Django management script
│   │   ├── 📄 db.sqlite3              # Database (created after migrate)
│   │   │
│   │   ├── creditproject/             # Project Settings
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 settings.py         # Django configuration
│   │   │   ├── 📄 urls.py             # URL routing
│   │   │   └── 📄 wsgi.py             # WSGI application
│   │   │
│   │   ├── users/                     # User Authentication App
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 apps.py             # App configuration
│   │   │   ├── 📄 models.py           # User models
│   │   │   ├── 📄 views.py            # Authentication views
│   │   │   ├── 📄 serializers.py      # DRF serializers
│   │   │   ├── 📄 urls.py             # App URLs
│   │   │   ├── 📄 signals.py          # Django signals
│   │   │   │
│   │   │   └── migrations/            # Database migrations
│   │   │       └── 📄 __init__.py
│   │   │
│   │   └── predictor/                 # Prediction API App
│   │       ├── 📄 __init__.py
│   │       ├── 📄 apps.py             # App configuration
│   │       ├── 📄 models.py           # Prediction history model
│   │       ├── 📄 views.py            # Prediction API views
│   │       ├── 📄 serializers.py      # Input/output serializers
│   │       ├── 📄 urls.py             # App URLs
│   │       ├── 📄 prediction_model.py # ML model interface
│   │       │
│   │       └── migrations/            # Database migrations
│   │           ├── 📄 __init__.py
│   │           └── 📄 0001_initial.py
│   │
│   └── ml_model/                      # Machine Learning Models
│       ├── 📄 train_model.py          # ML training script
│       ├── 📄 model.pkl               # ✅ Trained Random Forest model
│       ├── 📄 scaler.pkl              # ✅ Feature StandardScaler
│       ├── 📄 encoders.pkl            # ✅ LabelEncoders for categories
│       └── 📄 feature_names.pkl       # ✅ Feature names list
│
└── 📦 streamlit_app/                  # Streamlit Frontend
    └── 📄 app.py                      # Main Streamlit application
```

## 📄 Key Files Explained

### Batch Scripts (Windows Automation)

| File | Purpose | Command |
|------|---------|---------|
| `setup.bat` | **Initial one-time setup** | `setup.bat` |
| `run-django.bat` | Start Django backend (Terminal 1) | `run-django.bat` |
| `run-streamlit.bat` | Start Streamlit frontend (Terminal 2) | `run-streamlit.bat` |
| `verify.bat` | Check installation status | `verify.bat` |
| `init-db.bat` | Create superuser for admin | `init-db.bat` |

### Configuration Files

| File | Purpose |
|------|---------|
| `requirements.txt` | All Python dependencies |
| `.gitignore` | Files to ignore in git |
| `README.md` | Complete documentation |
| `QUICKSTART.md` | 5-minute quick start |
| `COMPLETE_SETUP.md` | Comprehensive setup guide |
| `ARCHITECTURE.md` | System design & architecture |

## 🔧 Django Applications

### 1. `users/` - User Management
**Location**: `credit_app/creditproject/users/`

| File | Purpose |
|------|---------|
| `models.py` | User model definitions |
| `views.py` | Registration, login, logout, profile |
| `serializers.py` | Data validation & serialization |
| `urls.py` | URL endpoints |
| `signals.py` | Auto token creation |
| `apps.py` | App configuration |

**Endpoints**:
- `POST /api/users/register/` - Register new user
- `POST /api/users/login/` - Login & get token
- `POST /api/users/logout/` - Logout user
- `GET /api/users/profile/` - Get user info

### 2. `predictor/` - Prediction API
**Location**: `credit_app/creditproject/predictor/`

| File | Purpose |
|------|---------|
| `models.py` | PredictionHistory model |
| `views.py` | Prediction endpoint |
| `serializers.py` | Request/response serialization |
| `urls.py` | URL endpoints |
| `prediction_model.py` | ML model loader & predictor |
| `apps.py` | App configuration |
| `migrations/` | Database migration files |

**Endpoints**:
- `POST /api/predictor/predict/` - Make prediction
- `GET /api/predictor/history/` - Get all predictions

### 3. Core Django Configuration
**Location**: `credit_app/creditproject/creditproject/`

| File | Purpose |
|------|---------|
| `settings.py` | Django configuration & installed apps |
| `urls.py` | URL routing & API routes |
| `wsgi.py` | WSGI application for deployment |
| `__init__.py` | Package marker |

## 🎨 Frontend Application

### Streamlit App
**Location**: `streamlit_app/app.py`

**Features**:
- Navigation bar with multi-page routing
- Home page with welcome & features
- Registration page with form validation
- Login page with authentication
- Predictor page (main feature)
- History page to view past predictions
- Profile page for user info
- Professional styling with CSS

**Pages**:
1. **Home** - Welcome screen
2. **Register** - New user registration
3. **Login** - User authentication
4. **Predictor** - Make predictions
5. **History** - View prediction history
6. **Profile** - User account info

## 🧠 Machine Learning

### ML Model System
**Location**: `credit_app/ml_model/`

#### `train_model.py`
- Loads dataset from Excel
- Preprocesses data (missing values, encoding)
- Trains Random Forest model
- Evaluates performance
- Saves model artifacts

#### Model Artifacts (Generated After Training)
| File | Purpose | Size |
|------|---------|------|
| `model.pkl` | Trained RandomForestClassifier | ~50MB |
| `scaler.pkl` | StandardScaler for features | ~1KB |
| `encoders.pkl` | LabelEncoders for categories | ~5KB |
| `feature_names.pkl` | Feature column names | ~1KB |

## 📊 Database Schema

### Tables (Auto-created by Django)

#### `auth_user` (Django built-in)
```sql
- id (PK)
- username (unique)
- email
- password (hashed)
- first_name
- last_name
- is_staff
- is_active
- date_joined
```

#### `authtoken_token` (Django REST Framework)
```sql
- key (PK) - Token string
- user_id (FK) - Reference to auth_user
- created - Creation timestamp
```

#### `predictor_predictionhistory` (Custom)
```sql
- id (PK)
- user_id (FK) - Reference to auth_user
- age
- income
- credit_score
- credit_utilization
- missed_payments
- loan_balance
- debt_to_income_ratio
- employment_status
- account_tenure
- credit_card_type
- location
- prediction (0 or 1)
- probability (0.0 to 1.0)
- created_at (timestamp)
```

## 🔄 Data Flow Architecture

```
User Input (Browser)
    ↓
Streamlit App (streamlit_app/app.py)
    ↓ HTTP Request
Django REST API (credit_app/creditproject/)
    ├───→ Users App (Authentication)
    └───→ Predictor App (Predictions)
    ↓ Check Authentication
Django Auth Token (authtoken_token table)
    ↓
SQLite Database (db.sqlite3)
    ├── User data
    └── Prediction history
    ↓ (for predictions)
ML Model (credit_app/ml_model/)
    ├── model.pkl
    ├── scaler.pkl
    └── encoders.pkl
    ↓ Prediction Result
Response to Streamlit
    ↓
Display in Browser
```

## 🚀 Execution Flow

### Initialization Sequence
```
1. setup.bat (One-time)
   ├─ Create venv
   ├─ Install dependencies
   ├─ Train ML model ✓
   └─ Initialize Django

2. Django Startup (run-django.bat)
   ├─ Load settings
   ├─ Initialize database
   ├─ Load apps
   └─ Start dev server (port 8000)

3. Streamlit Startup (run-streamlit.bat)
   ├─ Load app.py
   ├─ Initialize session state
   ├─ Connect to Django API
   └─ Open browser (port 8501)

4. User Interaction
   ├─ Register → POST to /api/users/register/
   ├─ Login → POST to /api/users/login/
   ├─ Predict → POST to /api/predictor/predict/
   └─ History → GET /api/predictor/history/
```

## 📈 Model Training Pipeline

```
trainining_model.py
    ↓
Load Dataset (Excel)
    ↓
Data Preprocessing
    ├─ Handle missing values
    ├─ Encode categories
    └─ Map payment status
    ↓
Feature Preparation
    ├─ Separate X & y
    ├─ Train-test split
    └─ Scale features
    ↓
Model Training
    ├─ RandomForest (100 trees)
    ├─ Max depth: 15
    └─ Min samples: 5
    ↓
Model Evaluation
    ├─ Accuracy: ~90%+
    ├─ ROC-AUC: ~95%+
    └─ Print metrics
    ↓
Save Artifacts
    ├─ model.pkl
    ├─ scaler.pkl
    ├─ encoders.pkl
    └─ feature_names.pkl
```

## 💾 File Sizes (Approximate)

| File | Size | Type |
|------|------|------|
| `model.pkl` | 50 MB | Binary (ML Model) |
| `scaler.pkl` | 1 KB | Binary (Scaler) |
| `encoders.pkl` | 5 KB | Binary (Encoders) |
| `db.sqlite3` | 100 KB | Binary (Database) |
| `app.py` | 50 KB | Python (Frontend) |
| `settings.py` | 5 KB | Python (Config) |
| `train_model.py` | 10 KB | Python (Script) |

**Total Project Size**: ~52 MB (including model)

## 🔐 Security File Locations

| Security Element | Location |
|------------------|----------|
| User Passwords | `db.sqlite3` (hashed) |
| Auth Tokens | `db.sqlite3` (encrypted in memory) |
| ML Model | `credit_app/ml_model/model.pkl` (binary) |
| Database | `credit_app/creditproject/db.sqlite3` (SQLite) |
| Credentials | `creditproject/settings.py` (SECRET_KEY) |

## 📝 Documentation Files

| File | Purpose | Audience |
|------|---------|----------|
| `README.md` | Complete documentation | Developers |
| `QUICKSTART.md` | 5-minute setup | First-time users |
| `COMPLETE_SETUP.md` | Full setup guide | Technical users |
| `ARCHITECTURE.md` | System design | Architects |
| `PROJECT_STRUCTURE.md` | This file | Code explorers |

## 🎓 Learning Path

1. **Start Here**: `QUICKSTART.md` - Get it running
2. **Understand**: `README.md` - Features & usage
3. **Deep Dive**: `ARCHITECTURE.md` - How it works
4. **Code**: `PROJECT_STRUCTURE.md` - Where things are
5. **Explore**: Review individual Python files

---

**Version**: 1.0  
**Last Updated**: March 2024  
**Status**: ✅ Complete & Ready to Use

---

### Next Steps
1. Follow `QUICKSTART.md` to get started
2. Run `setup.bat` to initialize
3. Start Django and Streamlit
4. Open http://localhost:8501
5. Register and make predictions!
