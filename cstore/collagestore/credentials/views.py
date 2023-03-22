from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.





def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('credentials:form')
        else:
            messages.info(request, 'username or password incorrect')
            return redirect('credentials:login')
    else:
        return render(request, 'login.html')

def register(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password == c_password:
            print("password check")
            if User.objects.filter(username=username):
                print("already exist")
                messages.info(request, "username allready exists")
                return redirect('credentials:register')

            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                print("user created")
                return redirect('credentials:login')
        else:
            print("passsword do not match")
            messages.info(request, 'Password dose not match')
            return redirect('credentials:register')
    return render(request, 'register.html')

def form(request):
    return render(request, 'form.html')