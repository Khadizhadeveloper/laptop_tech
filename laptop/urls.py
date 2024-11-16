from django.urls import path
from .views import *
from . import views



urlpatterns = [
    path('home/', views.home, name='home'),
    path('all/', LaptopList.as_view(), name='laptop-list'),
    path('<int:pk>/', LaptopDetail.as_view(), name='laptop-detail'),
    path('<int:pk>/delete', LaptopDelete.as_view(), name='laptop-delete'),
    path('<int:pk>/update', LaptopUpdate.as_view(), name='laptop-update'),
    path('rate/<int:product_id>/', rate_laptop, name='rate_product'),
    path('order/list/', OrderListView.as_view(), name='order-list'),
    path('order/', OrderCreateView.as_view(), name='order-create'),

]