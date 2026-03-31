from django.shortcuts import render
from app3.forms import Registration

# Create your views here.

def registration_form(req):
    fm=Registration()
    return render(req,'app3/register.html',{'form':fm})