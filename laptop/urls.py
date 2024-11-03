from django.urls import path
from .views import LaptopListCreate, LaptopDetailUpdateDelete



urlpatterns = [
    path('', LaptopListCreate.as_view(), name='laptop-list-create'),
    path('<int:pk>/', LaptopDetailUpdateDelete.as_view(), name='laptop-detail-update-delete'),
]