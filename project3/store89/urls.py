from django.urls import path
from .views import *
 
urlpatterns = [
    path('index/',index,name='index'),
    path('product/',product,name='product'),
    path('blog/',blog,name='blog'),
    path('blog_detail/',blog_detail,name='blog_detail'),
    path('contact/',contact,name='contact'),
    path('',home_02,name='home_02'),
    path('home_03/',home_03,name='home_03'),
    path('about/',about,name='about'),
    path('product_detail/',product_detail,name='product_detail'),
    path('shoping_cart/',shoping_cart,name='shoping_cart'),
    path('register/',register,name='register'),
    path('add_product/',add_product,name='add_product'),
    path('login/',login,name='login'),
]