from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('result/', views.process),
    path('result/display/', views.display),
    path('result/display/back/', views.back)
]