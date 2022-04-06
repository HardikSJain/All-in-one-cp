from unicodedata import name
from django.contrib import admin
from django.urls import include, path
from all_in_one_cp import views
urlpatterns = [

    path('', views.index, name="home"),
]
