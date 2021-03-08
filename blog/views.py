from django.shortcuts import render
from .models import post
from django.contrib.auth.models import User
# Create your views here.
def Home (request):
    #query data from models
    data=post.objects.all()
    return render(request,'index.html',{'posts':data})
   

def page1 (request):
    return render (request,'page1.html')

def createForm (request):
    return render (request,'form.html')

def addblog (request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['re-password']
    
    user=User.objects.create_user(
        username=username,
        password=password,
        first_name=firstname,
        last_name=lastname
        )
    user.save()
    return render (request,'result.html')