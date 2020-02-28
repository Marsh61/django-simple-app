from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1> Hello World </h1>")

def second_page_view(*args, **kwargs): 
    print(args,kwargs)
    print(len(args))
    print(args[0].user) # first argument is request 
    return render(args[0],"home.html",{}) #first request, second template file, third context 

def third_page_view(request,*args, **kwargs):
    context = {
        "text": "this is the text feild",
        "number": "123",
        "list": [12,"hi"]
    } 
    return render(request,"page_3.html",context) 
