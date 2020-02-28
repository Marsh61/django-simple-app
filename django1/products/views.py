from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ProductForm, RawProductForm

# Create your views here.

from .models import Product
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'obj': obj
    }
    return render(request,"products/detail.html",context)

def product_create_view(request):
    init_data = {
        'title': "My title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj) 
    if form.is_valid():
        form.save()
    
    context = {
        'form': form
    }
    return render(request, "products/product_create.html",context)

def product_raw_create_view(request):
    form = RawProductForm()
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(title=form.cleaned_data['title'],description= form.cleaned_data['description'], price=form.cleaned_data['price'])
    context = {
        "form": form
    }
    return render(request, "products/product_create2.html",context)
@csrf_exempt
def dynamic_lookup_view(request,id):
    if request.method == "DELETE":
        try:
            obj = Product.objects.get(id=id)
            obj.delete()
            return HttpResponse('{deleted: true}')
        except Product.DoesNotExist:
            raise Http404
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "obj": obj
    }
    return render(request, "products/product_detail.html",context)
    
@csrf_exempt
def dynamic_lookup_view(request,id):
    if request.method == "DELETE":
        try:
            obj = Product.objects.get(id=id)
            obj.delete()
            return HttpResponse('{deleted: true}')
        except Product.DoesNotExist:
            raise Http404
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "obj": obj
    }
    return render(request, "products/product_detail.html",context)

@csrf_exempt
def list_products_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html",context)