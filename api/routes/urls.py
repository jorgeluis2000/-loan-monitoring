from django.urls import path, include

urlpatterns = [
    path('crud/',include('api.routes.crud.urls'))
]
