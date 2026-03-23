import joblib
import numpy as np
import os
from django.conf import settings
from pathlib import Path

class PredictionModel:
    _model = None
    _label_encoders = None
    
    @classmethod
    def load_model(cls):
        if cls._model is None:
            # Navigate from creditproject to ml_model
            # BASE_DIR = e:\Credit Delinquncy\credit_app\creditproject
            # We need: e:\Credit Delinquncy\credit_app\ml_model
            ml_model_dir = Path(settings.BASE_DIR).parent / 'ml_model'
            model_path = ml_model_dir / 'model.pkl'
            encoder_path = ml_model_dir / 'encoders.pkl'
            scaler_path = ml_model_dir / 'scaler.pkl'
            
            try:
                if model_path.exists():
                    cls._model = joblib.load(str(model_path))
                    print(f"Model loaded from: {model_path}")
                else:
                    print(f"Model file not found at: {model_path}")
                    
                if encoder_path.exists():
                    cls._label_encoders = joblib.load(str(encoder_path))
                    print(f"Encoders loaded from: {encoder_path}")
                else:
                    print(f"Encoders not found at: {encoder_path}")
                    
                if scaler_path.exists() and cls._model is not None:
                    cls._scaler = joblib.load(str(scaler_path))
                    print(f"Scaler loaded from: {scaler_path}")
            except Exception as e:
                print(f"Error loading model files: {str(e)}")
                cls._model = None
        
        return cls._model, cls._label_encoders
    
    @classmethod
    def predict(cls, data):
        model, encoders = cls.load_model()
        
        if model is None:
            return None, None
        
        try:
            # Load scaler
            ml_model_dir = Path(settings.BASE_DIR).parent / 'ml_model'
            scaler_path = ml_model_dir / 'scaler.pkl'
            scaler = joblib.load(str(scaler_path)) if scaler_path.exists() else None
            
            # Prepare all 17 features in the correct order
            # Based on training: Age, Income, Credit_Score, Credit_Utilization, 
            # Missed_Payments, Loan_Balance, Debt_to_Income_Ratio, 
            # Employment_Status, Account_Tenure, Credit_Card_Type, Location,
            # Month_1 through Month_6
            
            # Encode categorical features
            employment_encoded = 0  # Default
            if encoders and 'Employment_Status' in encoders:
                try:
                    employment_encoded = encoders['Employment_Status'].transform([data['employment_status']])[0]
                except:
                    employment_encoded = 0
            
            card_type_encoded = 0  # Default
            if encoders and 'Credit_Card_Type' in encoders:
                try:
                    card_type_encoded = encoders['Credit_Card_Type'].transform([data['credit_card_type']])[0]
                except:
                    card_type_encoded = 0
            
            location_encoded = 0  # Default
            if encoders and 'Location' in encoders:
                try:
                    location_encoded = encoders['Location'].transform([data['location']])[0]
                except:
                    location_encoded = 0
            
            # Payment status mapping: On-time=0, Late=1, Missed=2
            payment_mapping = {'On-time': 0, 'Late': 1, 'Missed': 2}
            month_statuses = [2, 2, 2, 2, 2, 2]  # Default to Missed (2)
            
            # Prepare feature vector with all 17 features
            features = np.array([[
                data['age'],                           # 0
                data['income'],                        # 1
                data['credit_score'],                  # 2
                data['credit_utilization'],            # 3
                data['missed_payments'],               # 4
                data['loan_balance'],                  # 5
                data['debt_to_income_ratio'],          # 6
                employment_encoded,                    # 7
                data['account_tenure'],                # 8
                card_type_encoded,                     # 9
                location_encoded,                      # 10
                month_statuses[0],                     # 11 - Month_1
                month_statuses[1],                     # 12 - Month_2
                month_statuses[2],                     # 13 - Month_3
                month_statuses[3],                     # 14 - Month_4
                month_statuses[4],                     # 15 - Month_5
                month_statuses[5],                     # 16 - Month_6
            ]])
            
            # Scale features
            if scaler is not None:
                features = scaler.transform(features)
            
            # Make prediction
            prediction = model.predict(features)[0]
            probability = model.predict_proba(features)[0][1]
            
            return int(prediction), float(probability)
        except Exception as e:
            print(f"Error in prediction: {str(e)}")
            import traceback
            traceback.print_exc()
            return None, None
