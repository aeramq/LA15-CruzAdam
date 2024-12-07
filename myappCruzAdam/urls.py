from django.urls import path
from . import views

#URL Configuration
urlpatterns = [
    path('hello/', views.say_hello),
    path('hi/', views.say_hi),
    path('post/', views.blog_list, name='blog_list'),
    path('post/<id>/', views.blog_detail, name='blog_detail'),
]