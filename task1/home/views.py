from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import extended_user

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
                    return HttpResponse('hello')
                else:
                    if User.objects.filter(email=email,password=password).exists():
                        client=User.objects.get(email=email)
                        login(request, client)
                        return HttpResponse ('Hi')
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
            #photo= request.POST['file']
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
                reg = extended_user.objects.create(user=user,address=address,profile_pic=request.FILES['file'])
                reg.save()
                return HttpResponse('Succesful')
    else:
        logout_view(request)
    return render(request,'sign_up.html')


def logout_view(request):
    logout(request)
    return redirect('/')