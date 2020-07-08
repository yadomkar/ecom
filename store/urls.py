from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
	# path('', home, name='home'),
    path('', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),

    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),

    path('products/', products, name='products'),
    path('add_product/', addProduct, name='addProduct'),
    path('update_product/<str:pk>/', updateProduct, name='updateProduct'),
    path('delete_product/<str:pk>/', deleteProduct, name='deleteProduct'),
    # path('confirm_order/', confirmOrder, name='confirm_order'),
    # path('order_status/', payment_status, name='order_status'),
]
