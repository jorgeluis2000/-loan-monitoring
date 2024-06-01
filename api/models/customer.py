from django.db import models
from utils.constants.status import STATUS_CUSTOMER
# Create your models here.
class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    external_id = models.CharField(unique=True, max_length=60)
    status = models.PositiveSmallIntegerField(default=1,choices=STATUS_CUSTOMER)
    score = models.DecimalField(max_digits=12, decimal_places=2)
    preapproved_at = models.DateTimeField(auto_now=True)