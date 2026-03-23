from django.db import models

class PredictionHistory(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='predictions')
    age = models.IntegerField()
    income = models.FloatField()
    credit_score = models.FloatField()
    credit_utilization = models.FloatField()
    missed_payments = models.IntegerField()
    loan_balance = models.FloatField()
    debt_to_income_ratio = models.FloatField()
    employment_status = models.CharField(max_length=50)
    account_tenure = models.IntegerField()
    credit_card_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    
    prediction = models.IntegerField()  # 0 or 1
    probability = models.FloatField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Prediction for {self.user.username} - {self.created_at}"
