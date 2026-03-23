"""
ML Model Training Script for Credit Delinquency Prediction
This script trains a machine learning model on the delinquency dataset
and saves it for use in the prediction API.
"""

import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, accuracy_score
import warnings
warnings.filterwarnings('ignore')

def load_and_preprocess_data(dataset_path):
    """Load and preprocess the dataset"""
    print("Loading dataset...")
    df = pd.read_excel(dataset_path)
    
    print(f"Dataset shape: {df.shape}")
    print(f"Missing values:\n{df.isnull().sum()}\n")
    
    # Handle missing values
    df['Income'].fillna(df['Income'].median(), inplace=True)
    df['Credit_Score'].fillna(df['Credit_Score'].median(), inplace=True)
    df['Loan_Balance'].fillna(df['Loan_Balance'].median(), inplace=True)
    
    # Drop Customer_ID as it's not needed for prediction
    df = df.drop('Customer_ID', axis=1)
    
    # Target variable
    target = 'Delinquent_Account'
    
    # Features for encoding
    categorical_features = ['Employment_Status', 'Credit_Card_Type', 'Location']
    
    # Encode categorical variables
    label_encoders = {}
    for feature in categorical_features:
        le = LabelEncoder()
        df[feature] = le.fit_transform(df[feature])
        label_encoders[feature] = le
    
    # Handle payment status columns (Month_1 to Month_6)
    # Convert to numerical: On-time=0, Late=1, Missed=2
    payment_mapping = {'On-time': 0, 'Late': 1, 'Missed': 2}
    for month_col in ['Month_1', 'Month_2', 'Month_3', 'Month_4', 'Month_5', 'Month_6']:
        df[month_col] = df[month_col].map(payment_mapping)
    
    print("Data preprocessing completed!")
    
    return df, target, label_encoders

def train_model(df, target, label_encoders):
    """Train the prediction model"""
    print("\nPreparing features and target...")
    
    # Separate features and target
    X = df.drop(target, axis=1)
    y = df[target]
    
    print(f"Features shape: {X.shape}")
    print(f"Target shape: {y.shape}")
    print(f"Target distribution:\n{y.value_counts()}\n")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Random Forest model
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train_scaled, y_train)
    
    # Evaluate model
    print("\nModel Evaluation:")
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
    
    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"ROC-AUC Score: {roc_auc:.4f}")
    print(f"\nClassification Report:\n{classification_report(y_test, y_pred)}")
    print(f"\nConfusion Matrix:\n{confusion_matrix(y_test, y_pred)}\n")
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    print("Top 10 Important Features:")
    print(feature_importance.head(10))
    
    return model, scaler, label_encoders, X.columns

def save_model(model, scaler, label_encoders, feature_names, save_path):
    """Save the trained model and preprocessing objects"""
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    model_file = os.path.join(save_path, 'model.pkl')
    scaler_file = os.path.join(save_path, 'scaler.pkl')
    encoder_file = os.path.join(save_path, 'encoders.pkl')
    features_file = os.path.join(save_path, 'feature_names.pkl')
    
    joblib.dump(model, model_file)
    joblib.dump(scaler, scaler_file)
    joblib.dump(label_encoders, encoder_file)
    joblib.dump(feature_names, features_file)
    
    print(f"\nModel saved successfully!")
    print(f"Model path: {model_file}")
    print(f"Scaler path: {scaler_file}")
    print(f"Encoders path: {encoder_file}")
    print(f"Features path: {features_file}")

def main():
    """Main function to train and save the model"""
    # Dataset path
    dataset_path = r'd:\3RD SEM NOTES\Delinquency_prediction_dataset.xlsx'
    
    # Model save path
    save_path = os.path.dirname(os.path.abspath(__file__))
    
    print("="*60)
    print("Credit Delinquency Prediction - Model Training")
    print("="*60)
    
    # Load and preprocess data
    df, target, label_encoders = load_and_preprocess_data(dataset_path)
    
    # Train model
    model, scaler, label_encoders, feature_names = train_model(df, target, label_encoders)
    
    # Save model
    save_model(model, scaler, label_encoders, feature_names, save_path)
    
    print("\n" + "="*60)
    print("Training completed successfully!")
    print("="*60)

if __name__ == '__main__':
    main()
