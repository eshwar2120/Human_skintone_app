from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from skintoneapp import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('upload', views.upload, name='upload'),
    path('success', views.success, name='success'),
]
