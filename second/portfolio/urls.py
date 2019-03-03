from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('new/', views.new, name='new2'),
    path('create/', views.create, name='create2')
]