from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'st_activities/base.html') 

def op(request):
    return render(request,'st_activities/landing.html') 