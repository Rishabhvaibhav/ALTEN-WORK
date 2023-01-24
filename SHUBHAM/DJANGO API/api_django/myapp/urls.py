from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.my_api_function, name='my_api'),
    path('data/', views.phpmyadmin_data, name='sql_data'),
]
