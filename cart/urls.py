from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('add/<product_id>)/',views.cart_add, name='cart_add'),
    path('remove/<product_id>)/',views.cart_remove, name='cart_remove'),
]

"""
URL - View - Template
localhost/cart/ - cart_detail - detail.html
localhost/cart/add/product_id/ - cart_add
localhost/cart/remove/product_id/ - cart_remove
"""