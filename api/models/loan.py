from django.db import models
from .customer import Customer
from utils.constants.status import STATUS_LOAN

# Create your models here.
class Loan(models.Model):
    external_id = models.CharField(unique=True, max_length=60)
    amount = models.DecimalField(max_digits=12,decimal_places=2)
    score = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.PositiveSmallIntegerField(default=1,choices=STATUS_LOAN)
    contract_version = models.CharField(max_length=30)
    maximum_payment_date = models.DateTimeField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    take_at = models.DateTimeField()
    updated_at  = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    outstanding = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    
    def __str__(self) -> str:
        return self.external_id + ' - ' + self.customer_id.external_id