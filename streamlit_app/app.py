"""
Streamlit Frontend for Credit Delinquency Prediction App
Main app entry point with navigation
"""

import streamlit as st
import requests
import json
from datetime import datetime
import os

# Page configuration
st.set_page_config(
    page_title="Credit Delinquency Predictor",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stButton > button {
        width: 100%;
        padding: 10px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
    }
    .header-container {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        padding: 30px;
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
    }
    .info-box {
        background-color: #0f3460;
        color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #e94560;
        margin-bottom: 15px;
    }
    .success-box {
        background-color: #1a4d2e;
        color: white;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #52b788;
        margin-bottom: 15px;
    }
    .error-box {
        background-color: #5a1f1f;
        color: white;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #e94560;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# API Configuration
API_BASE_URL = "http://localhost:8000/api"

# Session state initialization
if 'token' not in st.session_state:
    st.session_state.token = None
if 'user' not in st.session_state:
    st.session_state.user = None
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def get_headers():
    """Get authorization headers"""
    headers = {"Content-Type": "application/json"}
    if st.session_state.token:
        headers["Authorization"] = f"Token {st.session_state.token}"
    return headers

def register_user(username, email, password, first_name, last_name):
    """Register a new user"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/users/register/",
            json={
                "username": username,
                "email": email,
                "password": password,
                "password2": password,
                "first_name": first_name,
                "last_name": last_name
            }
        )
        return response.json(), response.status_code
    except Exception as e:
        return {"error": str(e)}, 500

def login_user(username, password):
    """Login user"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/users/login/",
            json={"username": username, "password": password}
        )
        return response.json(), response.status_code
    except Exception as e:
        return {"error": str(e)}, 500

def logout_user():
    """Logout user"""
    try:
        requests.post(
            f"{API_BASE_URL}/users/logout/",
            headers=get_headers()
        )
    except:
        pass
    st.session_state.token = None
    st.session_state.user = None

def make_prediction(data):
    """Make a prediction"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/predictor/predict/",
            json=data,
            headers=get_headers()
        )
        return response.json(), response.status_code
    except Exception as e:
        return {"error": str(e)}, 500

def get_prediction_history():
    """Get prediction history"""
    try:
        response = requests.get(
            f"{API_BASE_URL}/predictor/history/",
            headers=get_headers()
        )
        return response.json(), response.status_code
    except Exception as e:
        return {"error": str(e)}, 500

# Navigation Bar
def show_navbar():
    """Display navigation bar"""
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.session_state.page = 'Home'
            st.rerun()
    
    if st.session_state.token:
        with col2:
            if st.button("🔮 Predictor", use_container_width=True):
                st.session_state.page = 'Predictor'
                st.rerun()
        
        with col3:
            if st.button("📊 History", use_container_width=True):
                st.session_state.page = 'History'
                st.rerun()
        
        with col4:
            if st.button("👤 Profile", use_container_width=True):
                st.session_state.page = 'Profile'
                st.rerun()
        
        with col5:
            if st.button("🚪 Logout", use_container_width=True):
                logout_user()
                st.session_state.page = 'Home'
                st.rerun()
    else:
        with col2:
            if st.button("📝 Register", use_container_width=True):
                st.session_state.page = 'Register'
                st.rerun()
        
        with col3:
            if st.button("🔐 Login", use_container_width=True):
                st.session_state.page = 'Login'
                st.rerun()
    
    st.divider()

# Pages
def home_page():
    """Home page"""
    st.markdown("""
        <div class="header-container">
            <h1>💳 Welcome to Credit Delinquency Predictor</h1>
            <p style="font-size: 18px;">Advanced AI-Powered Credit Risk Assessment</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-box">
            <h3>🎯 Our Mission</h3>
            <p>Predict credit delinquency risk with high accuracy using machine learning 
            and advanced analytics.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <h3>🔒 Secure & Private</h3>
            <p>Your data is encrypted and secure. We follow industry standards 
            for data protection.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-box">
            <h3>⚡ Fast Results</h3>
            <p>Get instant predictions on credit delinquency risk with detailed 
            risk assessment.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📋 About This Application")
    st.write("""
    This application uses machine learning to predict credit delinquency risk based on:
    
    - **Customer Demographics**: Age, Location
    - **Financial Metrics**: Income, Credit Score, Credit Utilization
    - **Credit History**: Missed Payments, Account Tenure, Loan Balance
    - **Employment Status**: Current employment information
    - **Payment Patterns**: Recent payment history
    
    The model is trained on comprehensive credit data and provides:
    - Accurate delinquency predictions
    - Risk level classification (Low, Medium, High)
    - Probability scores
    - Historical prediction tracking
    """)
    
    st.markdown("---")
    
    st.subheader("🚀 Getting Started")
    
    if not st.session_state.token:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Register New Account", use_container_width=True, key="home_register"):
                st.session_state.page = 'Register'
                st.rerun()
        with col2:
            if st.button("Login", use_container_width=True, key="home_login"):
                st.session_state.page = 'Login'
                st.rerun()
    else:
        st.info(f"✅ Logged in as: {st.session_state.user['username']}")
        if st.button("Go to Predictor", use_container_width=True):
            st.session_state.page = 'Predictor'
            st.rerun()

def register_page():
    """Registration page"""
    st.title("📝 Register")
    
    with st.form("register_form"):
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First Name")
        with col2:
            last_name = st.text_input("Last Name")
        
        username = st.text_input("Username", help="Choose a unique username")
        email = st.text_input("Email", help="Enter your email address")
        password = st.text_input("Password", type="password", help="Minimum 8 characters")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        submitted = st.form_submit_button("Register", use_container_width=True)
    
    if submitted:
        if not all([username, email, password, first_name, last_name]):
            st.error("❌ Please fill in all fields")
        elif password != confirm_password:
            st.error("❌ Passwords do not match")
        elif len(password) < 8:
            st.error("❌ Password must be at least 8 characters")
        else:
            result, status = register_user(username, email, password, first_name, last_name)
            
            if status == 201:
                st.session_state.token = result['token']
                st.session_state.user = result['user']
                st.success("✅ Registration successful! Redirecting to home...")
                st.balloons()
                st.session_state.page = 'Home'
                st.rerun()
            else:
                error_msg = result.get('error') or json.dumps(result)
                st.error(f"❌ Registration failed: {error_msg}")

def login_page():
    """Login page"""
    st.title("🔐 Login")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        submitted = st.form_submit_button("Login", use_container_width=True)
    
    if submitted:
        if not username or not password:
            st.error("❌ Please enter both username and password")
        else:
            result, status = login_user(username, password)
            
            if status == 200:
                st.session_state.token = result['token']
                st.session_state.user = result['user']
                st.success("✅ Login successful! Redirecting...")
                st.balloons()
                st.session_state.page = 'Home'
                st.rerun()
            else:
                st.error(f"❌ Login failed: {result.get('error', 'Invalid credentials')}")

def predictor_page():
    """Prediction page"""
    st.title("🔮 Credit Delinquency Predictor")
    
    st.info("Fill in the customer's information to predict credit delinquency risk")
    
    with st.form("prediction_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.number_input("Age", min_value=18, max_value=100, value=45)
            income = st.number_input("Annual Income ($)", min_value=0, value=50000)
            credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
        
        with col2:
            credit_utilization = st.slider("Credit Utilization (%)", 0, 100, 50)
            missed_payments = st.number_input("Missed Payments (Count)", min_value=0, max_value=50, value=0)
            loan_balance = st.number_input("Loan Balance ($)", min_value=0, value=10000)
        
        with col3:
            debt_to_income_ratio = st.slider("Debt-to-Income Ratio (%)", 0, 100, 30)
            account_tenure = st.number_input("Account Tenure (Years)", min_value=0, max_value=50, value=5)
            employment_status = st.selectbox(
                "Employment Status",
                ["Employed", "Self-Employed", "Unemployed", "Retired"]
            )
        
        credit_card_type = st.selectbox(
            "Credit Card Type",
            ["Platinum", "Gold", "Silver", "Standard"]
        )
        
        location = st.selectbox(
            "Location",
            ["Urban", "Suburban", "Rural"]
        )
        
        submitted = st.form_submit_button("Make Prediction", use_container_width=True)
    
    if submitted:
        prediction_data = {
            "age": age,
            "income": income,
            "credit_score": credit_score,
            "credit_utilization": credit_utilization,
            "missed_payments": missed_payments,
            "loan_balance": loan_balance,
            "debt_to_income_ratio": debt_to_income_ratio,
            "employment_status": employment_status,
            "account_tenure": account_tenure,
            "credit_card_type": credit_card_type,
            "location": location
        }
        
        result, status = make_prediction(prediction_data)
        
        if status == 200:
            col1, col2, col3 = st.columns(3)
            
            prediction = result['prediction']
            probability = result['probability']
            risk_level = result['risk_level']
            message = result['message']
            
            with col1:
                st.markdown(f"""
                <div class="success-box">
                    <h3>🎯 Prediction Result</h3>
                    <h2>{message}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="info-box">
                    <h3>📊 Risk Level</h3>
                    <h2>{risk_level}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="info-box">
                    <h3>📈 Probability</h3>
                    <h2>{probability}%</h2>
                </div>
                """, unsafe_allow_html=True)
            
            # Risk gauge
            st.progress(min(probability / 100, 1.0))
            st.caption(f"Delinquency Risk: {probability}%")
            
            st.success("✅ Prediction saved to your history!")
        else:
            error_msg = result.get('error') or json.dumps(result)
            st.error(f"❌ Prediction failed: {error_msg}")

def history_page():
    """Prediction history page"""
    st.title("📊 Prediction History")
    
    result, status = get_prediction_history()
    
    if status == 200 and result:
        st.info(f"Total predictions: {len(result)}")
        
        # Create a table with the prediction history
        for i, pred in enumerate(result[:10]):  # Show last 10
            with st.expander(f"Prediction {i+1} - {pred['created_at'][:10]}"):
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Age", pred['age'])
                    st.metric("Income", f"${pred['income']:,.0f}")
                
                with col2:
                    st.metric("Credit Score", pred['credit_score'])
                    st.metric("Missed Payments", pred['missed_payments'])
                
                with col3:
                    st.metric("Prediction", "Delinquent" if pred['prediction'] == 1 else "Not Delinquent")
                    st.metric("Risk Level", "High" if pred['probability'] > 0.7 else "Medium" if pred['probability'] > 0.4 else "Low")
                
                with col4:
                    st.metric("Probability", f"{pred['probability']*100:.2f}%")
    else:
        st.info("No predictions yet. Go to the Predictor to make your first prediction!")

def profile_page():
    """User profile page"""
    st.title("👤 User Profile")
    
    if st.session_state.user:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info-box">
                <h3>Account Information</h3>
            </div>
            """, unsafe_allow_html=True)
            
            st.write(f"**Username:** {st.session_state.user['username']}")
            st.write(f"**Email:** {st.session_state.user['email']}")
            st.write(f"**First Name:** {st.session_state.user['first_name']}")
            st.write(f"**Last Name:** {st.session_state.user['last_name']}")
            st.write(f"**User ID:** {st.session_state.user['id']}")
        
        with col2:
            st.markdown("""
            <div class="info-box">
                <h3>Account Status</h3>
            </div>
            """, unsafe_allow_html=True)
            
            st.success("✅ Active")
            st.info("You are logged in and can use all features")

# Main app
def main():
    show_navbar()
    
    # Route to pages
    if st.session_state.page == 'Home':
        home_page()
    elif st.session_state.page == 'Register':
        if st.session_state.token:
            st.session_state.page = 'Home'
            st.rerun()
        register_page()
    elif st.session_state.page == 'Login':
        if st.session_state.token:
            st.session_state.page = 'Home'
            st.rerun()
        login_page()
    elif st.session_state.page == 'Predictor':
        if not st.session_state.token:
            st.error("❌ Please login first to access the predictor")
            if st.button("Go to Login", use_container_width=True):
                st.session_state.page = 'Login'
                st.rerun()
        else:
            predictor_page()
    elif st.session_state.page == 'History':
        if not st.session_state.token:
            st.error("❌ Please login first to view history")
            if st.button("Go to Login", use_container_width=True):
                st.session_state.page = 'Login'
                st.rerun()
        else:
            history_page()
    elif st.session_state.page == 'Profile':
        if not st.session_state.token:
            st.error("❌ Please login first to view profile")
            if st.button("Go to Login", use_container_width=True):
                st.session_state.page = 'Login'
                st.rerun()
        else:
            profile_page()

if __name__ == '__main__':
    main()
