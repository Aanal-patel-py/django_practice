from django.contrib import admin
from django.urls import path,include

from app4 import views


urlpatterns = [
    path('debug/',views.test_debug,name='test_debug'),
   

]
