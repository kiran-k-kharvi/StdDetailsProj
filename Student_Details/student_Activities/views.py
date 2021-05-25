from django.shortcuts import render
from .forms import student_details_form,portfolio_form
from .models import student_Info
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.

def register(request):
    std_form = student_details_form()
    pofo_form = portfolio_form()
    if request.method == 'POST':
        std_form = student_details_form(request.POST)
        pofo_form = portfolio_form(data=request.POST,files=request.FILES) #or (data=request.POST, files=request.FILES)
        if std_form.is_valid() and pofo_form.is_valid():
            check_email = std_form.cleaned_data['Email']
            try:
                student_Info.objects.get(Email=check_email)
                return render(request,'st_activities/register.html',{"std":std_form,"pf":pofo_form,"em_error":"student with same email id already exist."})
            except student_Info.DoesNotExist:
                mod_std = std_form.save()
                mod_std.Password= make_password(mod_std.Password)
                mod_std.save()
                mod_pofo = pofo_form.save(commit=False)
                mod_pofo.student = mod_std
                mod_pofo.save()
                std_form = student_details_form()
                pofo_form = portfolio_form()
                return render(request,'st_activities/register.html',{"std":std_form,"pf":pofo_form,"msg":"Registered Successfully..."}) 
        else:
            return render(request,'st_activities/register.html',{"std":std_form,"pf":pofo_form,"valid_error":"Invalid form data"}) 

    else:
        return render(request,'st_activities/register.html',{"std":std_form,"pf":pofo_form})

def op(request):
    return render(request,'st_activities/login.html') 
