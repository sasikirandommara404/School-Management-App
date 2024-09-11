from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Q
from django.shortcuts import HttpResponse
from sasi.models import *
from django import template

# Create your views here.
def home(request):
    if request.method=="POST":
        Email=request.POST['email']
        Password=request.POST['password']
        valid=None
        try:
            valid=User.objects.get(email=Email)
        
            if valid.email==Email and valid.password==Password:
                if valid.is_staff==1:
                     return render(request,"adminhome.html")
                else:
                
        
                    return render(request,"main.html")
        except:
            return render(request,"login.html",{'s':'Wrong credential'})

      
        
       
    else:
        return render(request,"login.html")
def signup(request):
    if request.method=="POST":
        User_Name=request.POST['name']
        First_Name=request.POST['name1']
        Last_Name=request.POST['lastname']
        Email=request.POST['email']
        Password=request.POST['password']
        
        if User.objects.filter(email=Email):
            return render(request,"signup.html",{'ke':'All ready email exists'})
        else:
            user=User.objects.create(username=User_Name,first_name=First_Name,last_name=Last_Name,email=Email,password=Password)
            user.save()
            return redirect('home')

    else:
        return render(request,"signup.html")

def for_get(request):
    return render(request,"forget.html")
def update(request):
    if request.method=="POST":
        First_Name=request.POST['firstname']
        Last_Name=request.POST['lastname']
        Email=request.POST['email']
        Password=request.POST['password']
        try:
            up=User.objects.get(email=Email)
            up.first_name=First_Name
            up.last_name=Last_Name
            up.email=Email
            up.password=Password
            up.save()
            return redirect('home')
        except:
            return render(request,"forget.html",{'k':'ur email has not yet registerd'})
    
    else:
        return render(request,"forget.html")
def main(request):
    return render(request,"homepage.html")
def adminview(request):
    return render(request,"adminhome.html")
def student_details(request):
    return render(request,"studentupload.html")
def filling(request):
    if request.method=="POST":
        RollNumber=request.POST['rollnum']
        FirstName=request.POST['fname']
        LastName=request.POST['lname']
        PhoneNumber=request.POST['phone']
        Course=request.POST['course']
        Year=request.POST['year']
        Gender=request.POST['gender']
        City=request.POST['city']
        State=request.POST['state']
        stude=Student.objects.create(RollNumber=RollNumber,FirstName=FirstName,LastName=LastName,PhoneNumber=PhoneNumber,
                                    Course=Course,Year=Year,Gender=Gender,City=City,State=State)
        stude.save()
        return render(request,"studentupload.html")
def show(request):
    dis=Student.objects.all()
    return render(request,"display.html",{'key':dis})
def resup(request):
    return render(request,"resultsupload.html")
def results(request):
    RollNumber=request.POST['rollnum']
    Telugu=request.POST['tel']
    Hindi=request.POST['h']
    English=request.POST['e']
    Maths=request.POST['m']
    Physics=request.POST['p']
    Chemistry=request.POST['c']
    Science=request.POST['sc']
    Social=request.POST['s']
    re=Results.objects.create(RollNumber=RollNumber,Telugu=Telugu,Hindi=Hindi,English=English,Maths= Maths,
                              Physics=Physics,Chemistry=Chemistry,Science=Science,Social=Social)
    re.save()
    return render(request,"resultsupload.html")
def show1(request):
    dis=Student.objects.all()
    return render(request,"update.html",{'key':dis})
#RollNumber=None
def updateform(request):
    #global RollNumber
    if request.method=="POST":
        RollNumber=request.POST['roll']
        Email=request.POST['email']
        Password=request.POST['pass']
        try:
            se=User.objects.get(email=Email)
            if se.email==Email and se.password==Password:
                
                try:
                    hold=Student.objects.get(RollNumber=RollNumber)
                    return render(request,"up2.html",{'g':hold})
                    
    
                except:
                    return render(request,"up1.html",{'mg':'Invalid Rollnumber'})



               
        except:
            return render(request,"up1.html",{'msg':"Invalid Password"}) 


    else:
        return render(request,"up1.html") 
# def upd(request,)
def finall(request):
    RollNumber=request.POST['rollnum']
    FirstName=request.POST['fname']
    LastName=request.POST['lname']
    PhoneNumber=request.POST['phone']
    Course=request.POST['course']
    Year=request.POST['year']
    Gender=request.POST['gender']
    City=request.POST['city']
    State=request.POST['state']
    try:
        user=Student.objects.get(RollNumber=RollNumber)
        user.RollNumber=RollNumber
        user.FirstName=FirstName
        user.LastName=LastName
        user.PhoneNumber=PhoneNumber
        user.Course=Course
        user.Year=Year
        user.Gender=Gender
        user.City=City
        user.State=State
        user.save()
        return redirect('show1')
    except:
         return render(request,"up1.html",{'msg':"Invalid Password"}) 

def res_function(request):
    return render(request,"res.html")
def checking_res(request):
    RollNumber=request.POST['rollnumber']
    try:
        result=Results.objects.get(RollNumber=RollNumber)
        status="Pass"
        if result.Telugu>=35 and result.Hindi>=35 and result.English>=35 and result.Maths>=35 and result.Physics>=21 and result.Chemistry>=21 and result.Science>35 and result.Social>=35:
            status="Pass"
        else:
            status="Fail"  
        
        

        return render(request,"disres.html",{'ke':result,'s':status})
    except:
        return render(request,"res.html",{'kj':'Inavlid RollNumber'})




