# Generated migration
from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('income', models.FloatField()),
                ('credit_score', models.FloatField()),
                ('credit_utilization', models.FloatField()),
                ('missed_payments', models.IntegerField()),
                ('loan_balance', models.FloatField()),
                ('debt_to_income_ratio', models.FloatField()),
                ('employment_status', models.CharField(max_length=50)),
                ('account_tenure', models.IntegerField()),
                ('credit_card_type', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('prediction', models.IntegerField()),
                ('probability', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
