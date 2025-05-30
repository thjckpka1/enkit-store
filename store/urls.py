from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('software/<int:pk>/', views.software_detail, name='software_detail'),
]