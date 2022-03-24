from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import ClientRegistration
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

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




def logout_view(request):
    logout(request)
    return redirect('/')