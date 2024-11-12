from django.urls import path
from .views import LaptopListCreate, LaptopDetailUpdateDelete, OrderCreateView, OrderListView



urlpatterns = [
    path('', LaptopListCreate.as_view(), name='laptop-list-create'),
    path('<int:pk>/', LaptopDetailUpdateDelete.as_view(), name='laptop-detail-update-delete'),
    path('order/list/', OrderListView.as_view(), name='order-list'),
    path('order/', OrderCreateView.as_view(), name='order-create'),
]