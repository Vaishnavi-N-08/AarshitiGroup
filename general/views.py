from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from general.models import Feedback
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

def construction(request):
    return render(request, "construction.html")

def spices(request):
    return render(request, "spices.html")

def agrotech(request):
    return render(request, "agrotech.html")

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        log = request.POST.get('log')
        if log == "no":
            username = request.POST.get('userId')
            email = request.POST.get('emailId')
            password = request.POST.get('password')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=email, email=email, password=password, first_name=username)
                user.save()
                user = auth.authenticate(
                    username=email, email=email, password=password)
                auth.login(request, user)
                return redirect("home")
        else:
            email = request.POST.get('emailId')
            password = request.POST.get('password')
            user = auth.authenticate(
                username=email, email=email, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Invalid credentials")
                return redirect("register")
    else:
        return render(request, "register.html")

@login_required(login_url='/register')
def logout(request):
    auth.logout(request)
    return redirect('home')

def feedback(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        feedback = request.POST['feedback']
        new_feedback = Feedback(
            fullname=fullname, email=email, feedback=feedback)
        new_feedback.save()
        return redirect('feedback')
    else:
        return render(request, "feedback.html")