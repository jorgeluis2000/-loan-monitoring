from django.contrib import admin
from api.models.customer import Customer
from api.models.loan import Loan
from api.models.payment import Payment
from api.models.paymentdetail import PaymentDetail
# Register your models here.

admin.site.register(Customer)
admin.site.register(Loan)
admin.site.register(Payment)
admin.site.register(PaymentDetail)