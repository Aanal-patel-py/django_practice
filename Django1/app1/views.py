from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.
def myfunc(request):

    return HttpResponse("yo")

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

