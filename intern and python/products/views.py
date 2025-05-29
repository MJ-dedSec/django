from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all() # This line fetches all products from the database
    return render(request, 'index.html',  {'products': products}) 
def new(request):
    return HttpResponse('new products')

