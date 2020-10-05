from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return  HttpResponse('HI EVERY BODY')
    return render(request,"about.html")

def Home(request):
    return render(request,"home.html")
    # return HttpResponse('<a href = "http://www.tsetmc.com/Loader.aspx?ParTree=15">Home </a>')
