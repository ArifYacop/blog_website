from django.shortcuts import render

# Create your views here.
def Home (request):
    tags=['mother','father','brother','sister']
    rating=4
    return render (request,'index.html',
    {
        'name':'THE IKHLAS',
        'author':'ARIF YACOP',
        'tags':tags,
        'rating':rating
        })

def page1 (request):
    return render (request,'page1.html')

def createForm (request):
    return render (request,'form.html')

def addblog (request):
    name=request.GET['name']
    description=request.GET['description']
    return render (request,'result.html',{'name':name,'description':description})