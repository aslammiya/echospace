from django.shortcuts import render, redirect, HttpResponse
from .models import CustomUser
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    context = {'noIcons': range(150),
               'noSocialUser': range(20),
               'online': "green",
               'offline': "red",
               'name': "Aslam Miya",
               'username': "@aslammiya",
               'noOfUsers': 50
               }
    return render(request, "index.html", context)

def sign_up(request):
    if request.method == "POST":
        data = request.POST
        fname = data.get("first-name")
        lname = data.get("last-name")
        uname = data.get("username")
        paswd = data.get("password")
        profile_img = request.FILES.get("dp")

        print(fname, lname, uname, paswd, profile_img)
        new_user = CustomUser.objects.create(
            first_name=fname,
            last_name=lname,
            username=uname,
            password=paswd,
            profile_image=profile_img
        )
        new_user.set_password(paswd)
        new_user.save()

        return redirect("/login")
    return render(request, 'userRegistration.html')

def check_username(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        user_exists = CustomUser.objects.filter(username=username).exists()
        print(user_exists)
        return JsonResponse({'available': not user_exists})

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("/login")

    return render(request, "loginUser.html")

def sign_out(request):
    pass