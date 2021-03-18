from django.shortcuts import render,redirect
from .models import post
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def Home (request):
    #query data from models
    data=post.objects.all()
    return render(request,'index.html',{'posts':data})

def result (request):
    name=request.POST['name']
    desciption=request.POST['description']
    return render(request,'result.html',{'name':name,'description':desciption})
    
    
   

def page1 (request):
    return render (request,'page1.html')



def createForm (request):
    return render (request,'form.html')

def adduser (request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['re-password']
    
    if password==repassword :
        if User.objects.filter(username=username).exists():
            messages.info(request,'username มีคนใช้แล้ว')
            print("username มีคนใช้แล้ว")
            return redirect('/createForm')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email มีคนใช้แล้ว')
            print("email มีคนใช้แล้ว")
            return redirect('/createForm')
        else :
            messages.info(request,'รหัสผ่านไม่ตรงกัน')
            user=User.objects.create_user(
        username=username,
        password=password,
        first_name=firstname,
        last_name=lastname
        )
        user.save()
        return redirect('/Home')
    else : 
        return redirect('/createForm')

def loginForm (request):
    return render (request,'login.html')

def login(request):
    username=request.POST['username']
    password=request.POST['password']

    #Check username and password
    user=auth.authenticate(username=username,password=password)

    if user is not None :
        auth.login(request,user)
        return redirect('/Home')
    else:
         messages.info(request,'ไม่พบข้อมูล')
    return redirect('/loginForm')

def logout(request):
    auth.logout(request)
    return redirect('/Home')