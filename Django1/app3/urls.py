from django.urls import path,include
from app3 import views

urlpatterns = [
    path('register/',views.registration_form,name='registration_form'),

]