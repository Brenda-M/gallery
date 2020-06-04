from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='homepage')
  path('/details/<int:pk>/', views.details, name='image_details')
]