from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import authenticate , login

# Create your views here.
def index(request):
    return render(request,'index.html')  

def blog(request):
    return render(request,'blog.html')

def blog_detail(request):
    return render(request,'blog_detail.html')

def contact(request):
    return render(request,'contact.html')

def home_02(request):
    return render(request,'home_02.html')

def home_03(request):
    return render(request,'home_03.html')

def about(request):
    return render(request,'about.html')

def product_detail(request):
    return render(request,'product_detail.html')

def shoping_cart(request):
    return render(request,'shoping_cart.html')

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method=="POST":
        customer=CustomerForm(request.POST)
        if customer.is_valid():
            customer.save()
            return redirect('/login')
        else:
            return HttpResponse(request,"Registration falied ,invalid data")
    else:
        customer=CustomerForm()
    return render(request,'register.html',{"form":customer})



def add_product(request):
    if request.method == "POST":
        form = productForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/product')
        else:
            return HttpResponse(request,"invalid form data")
    else:
        form = productForm()    
    return render(request, 'add-product.html',{"form":form})   

def product(request):
    products = productsModoel.objects.all()
    return render(request,'product.html',{"products":products})



def login(request):
    if request.method == "POST":
        username =  request.POST.get('Name')
        password = request.POST.get('Pwd')

        user = authenticate(request,username = username , password = password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse(request,'invalid user or password')
    return render(request,'login.html')