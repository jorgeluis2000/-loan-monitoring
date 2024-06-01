from django.urls import path, include
from rest_framework import routers
from api.controllers.customer import CustomerViewSet
from api.controllers.loan import LoanViewSet

CrudRouter = routers.DefaultRouter()
CrudRouter.register(r'customers', viewset=CustomerViewSet)
CrudRouter.register(r'loans', viewset=LoanViewSet)

urlpatterns = [
    path('',include(CrudRouter.urls))
]
