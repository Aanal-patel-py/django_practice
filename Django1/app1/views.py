from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.
def myfunc(request):
    context={"user_name":"AANAL"}
    return render(request,"app1/abc.html",context)

def myfunc2(req,**kwargs):
    status=kwargs.get('status','not allowed')
    return HttpResponse(f'hello there {status}')
def post_detail(request, id):
    return HttpResponse(f"Post ID is {id}")

def data_insert(request):
    Person.objects.create(
        first_name='abc',
        last_name='xyz',
        address='abc appartments'
    )
    return HttpResponse("person details added")

def home(request):
    return render(request,"app1/base.html")
def page1(request):
    return render(request,"app1/page1.html")
def page2(request):
    return render(request,"app1/page2.html")


