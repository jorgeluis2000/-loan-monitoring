from django.urls import path, include
from rest_framework import routers
from api.controllers.customer import CustomerViewSet, create_customers_from_txt
from api.controllers.loan import LoanViewSet
from api.controllers.payment import PaymentViewSet
from api.controllers.login import LoginViewSet

# Configuración del erutado CRUD
CrudRouter = routers.DefaultRouter()
CrudRouter.register(r'customers', viewset=CustomerViewSet)
CrudRouter.register(r'loans', viewset=LoanViewSet)
CrudRouter.register(r'payments', viewset=PaymentViewSet)
CrudRouter.register(r'credentials', viewset=LoginViewSet)

# Definición de las URLs
urlpatterns = [
    # Incluir las URLs generadas por el erutado CRUD
    path('', include(CrudRouter.urls)),
    # Ruta para la creación de clientes desde un archivo de texto
    path('create-customer-from-txt/', create_customers_from_txt, name="create_customers_from_txt"),
]
