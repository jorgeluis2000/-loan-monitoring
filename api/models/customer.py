from django.db import models
from utils.constants.status import STATUS_CUSTOMER

class Customer(models.Model):
    """
    Modelo que representa a un cliente en el sistema.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(unique=True, max_length=60)
    status = models.PositiveSmallIntegerField(
        default=1, choices=STATUS_CUSTOMER)
    score = models.DecimalField(max_digits=12, decimal_places=2)
    preapproved_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """
        Método que devuelve una representación legible en cadena del objeto Customer.
        """
        return f'{self.id} - {self.external_id}'
