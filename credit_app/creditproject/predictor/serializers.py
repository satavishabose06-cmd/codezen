from rest_framework import serializers
from .models import PredictionHistory

class PredictionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionHistory
        fields = '__all__'
        read_only_fields = ['user', 'prediction', 'probability', 'created_at']

class PredictionRequestSerializer(serializers.Serializer):
    age = serializers.IntegerField(min_value=18, max_value=100)
    income = serializers.FloatField(min_value=0)
    credit_score = serializers.FloatField(min_value=300, max_value=850)
    credit_utilization = serializers.FloatField(min_value=0, max_value=100)
    missed_payments = serializers.IntegerField(min_value=0)
    loan_balance = serializers.FloatField(min_value=0)
    debt_to_income_ratio = serializers.FloatField(min_value=0, max_value=100)
    employment_status = serializers.CharField(max_length=50)
    account_tenure = serializers.IntegerField(min_value=0)
    credit_card_type = serializers.CharField(max_length=50)
    location = serializers.CharField(max_length=100)
