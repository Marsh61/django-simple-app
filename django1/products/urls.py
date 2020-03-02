from django.urls import path
from .views import (product_detail_view, 
product_create_view, 
product_raw_create_view, 
dynamic_lookup_view,
list_products_view
)
app_name = "products"
urlpatterns = [
    path('product',product_detail_view),
    path('create',product_create_view),
    path('raw_create',product_raw_create_view),
    path('<int:id>/',dynamic_lookup_view,name="product-view"),
    path('',list_products_view,name="blah"),
]