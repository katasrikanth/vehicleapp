from django.contrib import admin
from django.urls import path
from .views import listofvehicle,createvehicle,detailvehicle,updatevehicle,deletevehicle

urlpatterns = [
    path('', listofvehicle.as_view(),name="home"),
    path('create/',createvehicle.as_view(),name="new"),
    path('detail/<int:pk>/',detailvehicle.as_view(),name="detail"),
    path('update/<int:pk>',updatevehicle.as_view(),name="change"),
    path('delete/<int:pk>/',deletevehicle.as_view(),name="delete"),
]
