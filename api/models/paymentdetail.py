from django.db import models
from .loan import Loan  # Importación del modelo Loan
from .payment import Payment  # Importación del modelo Payment

class PaymentDetail(models.Model):
    """
    Modelo que representa un detalle de pago en el sistema.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """
        Método que devuelve una representación legible en cadena del objeto PaymentDetail.
        """
        return f'{self.loan_id.external_id} - {self.payment_id.external_id}'
