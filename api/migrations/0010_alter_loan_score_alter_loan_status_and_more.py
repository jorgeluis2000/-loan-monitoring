# Generated by Django 5.0.6 on 2024-06-02 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_loan_outstanding_alter_loan_customer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Pendiente'), (2, 'Activo'), (3, 'rechazado'), (4, 'Pagado')], default=2),
        ),
        migrations.AlterField(
            model_name='loan',
            name='take_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]