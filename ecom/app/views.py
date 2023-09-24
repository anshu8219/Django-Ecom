from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
# def home(request):
#  return render(request, 'app/home.html')

class Productview(View): 
    def get(self,request):
        Mobile = Product.objects.filter(category='M')
        Laptop = Product.objects.filter(category='L')
        Headphone = Product.objects.filter(category='L')
        return render (request,'app/home.html',
        {'Mobile':mobile,'Laptop':Laptop,'Headphone':Headphone}) 
    

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
