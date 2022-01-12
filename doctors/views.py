from django.shortcuts import render
from django.http import HttpResponse
from .models import doctors

# Create your views here.
def login(request):
    return render(request,'login.html')

def registrationValidation(request):
    name = request.POST['name']
    specality = request.POST['specality']
    gender = request.POST['gender']
    phone = request.POST['phone']
    password = request.POST['password']
    clinic_address = request.POST['clinic_address']
    submit_details=doctors(name=name,specality=specality,gender=gender,phone=phone,password=password,clinic_address=clinic_address)
    submit_details.save()
    return HttpResponse("Registration Successfull")

def loginauth(request):
    phone=request.POST['a']
    passw=request.POST['b']
    doctors_table=doctors.objects.all()
    for i in doctors_table:
        if(i.phone==phone and i.password==passw):
            # request.session['id']=i.id
            return  HttpResponse(1)
    return HttpResponse(0)



def doctorsDashboard(request):
    return render(request,'doctorDashboard.html')

def prescription(request):
    return render(request,'prescription.html')

def demotutorial(request):
    return HttpResponse("Hii ...")
