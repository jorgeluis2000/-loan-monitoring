# Generated by Django 5.0.6 on 2024-06-02 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_loan_score_alter_loan_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetail',
            name='loan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.loan'),
        ),
        migrations.AlterField(
            model_name='paymentdetail',
            name='payment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.payment'),
        ),
    ]