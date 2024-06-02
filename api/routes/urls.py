from django.urls import path, include
from rest_framework import routers
from api.controllers.customer import CustomerViewSet, create_customers_from_txt
from api.controllers.loan import LoanViewSet
from api.controllers.payment import PaymentViewSet

# Configuración del enrutador CRUD
CrudRouter = routers.DefaultRouter()
CrudRouter.register(r'customers', viewset=CustomerViewSet)
CrudRouter.register(r'loans', viewset=LoanViewSet)
CrudRouter.register(r'payments', viewset=PaymentViewSet)

# Definición de las URLs
urlpatterns = [
    # Incluir las URLs generadas por el enrutador CRUD
    path('', include(CrudRouter.urls)),
    # Ruta para la creación de clientes desde un archivo de texto
    path('create-customer-from-txt/', create_customers_from_txt, name="create_customers_from_txt")
]
