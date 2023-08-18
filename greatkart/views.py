from store.models import Product
from django.shortcuts import render

def home(request):
    products=Product.objects.all().filter(is_avilable=True)
    
    context={
        'products':products,
    }
    
    return render(request ,'home.html',context)