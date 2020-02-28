"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django1.pages.views import home_view
from django1.pages.views import second_page_view
from django1.pages.views import third_page_view
from django1.products.views import product_detail_view, product_create_view, product_raw_create_view, dynamic_lookup_view,list_products_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homie',home_view),
    path('2',second_page_view),
    path('3',third_page_view),
    path('product',product_detail_view),
    path('create',product_create_view),
    path('raw_create',product_raw_create_view),
    path('products/<int:id>/',dynamic_lookup_view,name="blah"),
    path('products',list_products_view,name="blah"),
]
