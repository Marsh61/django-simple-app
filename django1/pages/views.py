from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1> Hello World </h1>")

def second_page_view(*args, **kwargs): 
    print(args,kwargs)
    print(len(args))
    print(args[0].user) # first argument is a request
    return render(args[0],"home.html",{})