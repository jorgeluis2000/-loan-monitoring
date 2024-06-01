from django.db import models
from .loan import Loan
from .payment import Payment

# Create your models here.
class PaymentDetail(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    loan_id = models.ForeignKey(Loan, on_delete=models.DO_NOTHING)
    payment_id = models.ForeignKey(Payment, on_delete=models.DO_NOTHING)