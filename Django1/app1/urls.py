from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns = [
    path('myfun/', views.myfunc2, name='myfucn'),
    path('blah/',views.myfunc2,{'status':'ok'},name='myfunc2'),
    path("post/<int:id>/", views.post_detail, name="post_detail"),
    path("data/",views.data_insert,name="data_insert"),
    path("color/",views.data_insert,name="data_insert"),
    path("temp/",views.myfunc,name="myfunc"),
    path("home/page1/",views.page1,name="page1"),
    path("home/page2/",views.page2,name="page2"),
    path("home/",views.home,name="home"),

]
