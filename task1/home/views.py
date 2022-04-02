from datetime import datetime, timedelta
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Appointment, extended_user,Blog
import home.setup as setup

def logins(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            if User.objects.filter(email=email).exists():
                value=User.objects.get(email=email)
                username=value.username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/account/'+str(client.id))
                else:
                    if User.objects.filter(email=email,password=password).exists():
                        client=User.objects.get(email=email)
                        login(request, client)
                        return redirect('/account/'+str(client.id))
                    else:
                        messages.info(request,"Invalid Credentials")
            else:
                messages.info(request,"Invalid Credentials")
    else:
        logout_view(request)
    return render(request,'login.html')


def SignUp(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username = request.POST['uname']
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['password1']
            address= request.POST['address']
            type=False
            if request.POST.get('type') == "1":
                type=True
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Please Use Different Username")
            elif password!=confirm_password:
                messages.info(request,"Password's Didn't Matched")
            else:
                reg = User.objects.create(username=username, last_name=last_name, email=email, password=password,first_name=first_name)
                reg.save()
                user=User.objects.get(username=username)
                reg = extended_user.objects.create(user=user,address=address,profile_pic=request.FILES['file'],type=type)
                reg.save()
                messages.info(request,'You Have Succesfully Registered Please Login')
                return redirect('login')
    else:
        logout_view(request)
    return render(request,'sign_up.html')

def add_blog(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            title = request.POST['title']
            cat = request.POST['cat']
            summary = request.POST['summary']
            content = request.POST['content']
            type=False
            if request.POST.get('type') == "1":
                type=True
            name=request.user.username
            client=User.objects.get(username=name)
            reg = Blog.objects.create(title=title,category=cat,summary=summary,content=content,draft=type,image=request.FILES['file'],user=name)
            reg.save()
            return redirect('/account/'+str(client.id))
        return render(request,'add_blog.html')
    else:
        return redirect('login')

def client(request,id):
    if request.user.is_authenticated:
        client=User.objects.get(pk=id)
        user=extended_user.objects.get(user=client)
        if user.type:
            blog=Blog.objects.filter(user=client.username)
        else:    
            blog=Blog.objects.filter(draft=False)
        return render(request,'dashboard.html',{'client':client,'user':user,'blog':blog})
    else:
        return redirect('login')

def book(request,id):
    if request.user.is_authenticated:
        user=extended_user.objects.filter(type=True)
        return render(request,'doc.html',{'user':user})
    else:
        return redirect('login')

def done(request,id):
    if request.user.is_authenticated:
        user=Appointment.objects.get(id=id)
        time=user.time
        time=str(time)
        x=time.split(':')
        x[1]=int(x[1])+45
        endtime=str(x[0])+":"+str(x[1])
        return render(request,'booked.html',{'user':user,'endtime':endtime})
    else:
        return redirect('login')

def appoint(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            doctor = request.POST['doc']
            patient= request.POST['patient']
            speciality = request.POST['speciality']
            date = request.POST['date']
            time=request.POST['time']
            reg = Appointment.objects.create(doctor=doctor,patient=patient,speciality=speciality,date=date,time=time)
            reg.save()
            x=time.split(':')
            x[1]=int(x[1])+45
            endtime=str(x[0])+":"+str(x[1])
            template={
            "summary": "Appointment with "+doctor+"-"+patient+"speciality"+speciality,
            "description": "This a description",
            "start": {
                "dateTime": date+"T"+time+":00",
                "timeZone": "America/El_Salvador"
            },
            "end": {
                "dateTime": date+"T"+endtime+":00",
                "timeZone": "America/El_Salvador"
            },
            "attendees": [{ "email": "email@gmail.com" }],
            "reminders": {
                "useDefault": False,
                "overrides": [
                { "method": "email", "minutes": 30 },
                { "method": "popup", "minutes": 10 }
                ]
            }
            }
            setup.create_event(template)
            return redirect('/booked/'+str(reg.id))
        user=extended_user.objects.filter(type=True)
        client=User.objects.get(pk=id)
        setup.get_crendetials_google()
        return render(request,'appoint.html',{'user':user,'client':client})
    else:
        return redirect('login')

def show(request,id):
    if request.user.is_authenticated:
        blog=Blog.objects.get(id=id)
        client=User.objects.get(username=blog.user)
        user=extended_user.objects.get(user=client)
        str=blog.summary
        l=str.split(' ')
        s=''
        p=''
        if len(l)>15:
            for i in range(15):
                s=s+l[i]+' '
            for i in range(15,len(l)):
                p=p+l[i]+' '
        else:
            s=str
            p=False
        return render(request,'view.html',{'client':client,'user':user,'blog':blog,'s':s,'p':p})
    else:
        return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('/')