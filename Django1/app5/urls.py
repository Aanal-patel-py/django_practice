from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView

from app5 import views


urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.signin,name='signin'),
    path('logout/', LogoutView.as_view(next_page='signin'), name='logout'),
   

]
