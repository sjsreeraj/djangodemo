from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
def allcategories(request):
    c=Category.objects.all()

    return render(request,'category.html',{'c':c})

def allproducts(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request,'product.html',{'c':c,'p':p})
def details(request,p):
     c=Product.objects.get(name=p)
     return render(request,'details.html',{'c':c})

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']

        if(p==cp):
           user=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
           user.save()
           return redirect('shop:allcategories')
        else:
          return HttpResponse("not same")
    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:allcategories')
        else:
            return HttpResponse("Invalid")
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)





