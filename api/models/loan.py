from django.db import models
from .customer import Customer
from utils.constants.status import STATUS_LOAN

# Create your models here.
class Loan(models.Model):
    external_id = models.CharField(unique=True, max_length=60)
    amount = models.DecimalField(max_digits=12,decimal_places=2)
    score = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    status = models.PositiveSmallIntegerField(default=2,choices=STATUS_LOAN)
    contract_version = models.CharField(max_length=30)
    maximum_payment_date = models.DateTimeField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    outstanding = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    take_at = models.DateTimeField(auto_now=True)
    updated_at  = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.external_id} - {self.customer_id.external_id}'