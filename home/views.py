from django.shortcuts import render, redirect, HttpResponse
from .models import CustomUser
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
import random, string
from django.shortcuts import get_object_or_404

@csrf_protect
def sign_up(request):
    if request.method == "POST":
        data = request.POST
        fname = data.get("first-name")
        lname = data.get("last-name")
        uname = data.get("username")
        paswd = data.get("password")
        profile_img = request.FILES.get("dp")

        new_user = CustomUser.objects.create(
            first_name=fname,
            last_name=lname,
            username=uname,
            password=paswd,
            profile_image=profile_img,
            isGuest=False
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

@csrf_protect
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
    logout(request)
    return redirect("/login")

def genGuestCred():
    firstName = "User"
    while True:
        lastName = random.randint(1000, 9999)
        if CustomUser.objects.filter(last_name=lastName).exists():
            continue
        else:
            break
    guestUserName = (f"{firstName.lower()}{lastName}")
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    guestUserObject = CustomUser.objects.create(
        first_name=firstName,
        last_name=lastName,
        username=guestUserName
    )
    guestUserObject.set_password(password)
    guestUserObject.save()
    return guestUserName, password

@csrf_protect
def guest_login(request):
    guestUserName, password = genGuestCred()
    user = authenticate(username=guestUserName, password=password)
    if user is not None:
        login(request, user)
        return redirect("/")
    else:
        messages.error(request, "Failed to login as guest.")
        return redirect("/login")

@login_required(login_url="/login/")
def saveProfileInfo(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        firstName = data.get("first_name")
        lastName = data.get("last_name")
        user = get_object_or_404(CustomUser, username = request.user.username)
        
        user.first_name = firstName
        user.last_name = lastName
        user.username = username
        if request.FILES.get("dp"):
            user.profile_image = request.FILES.get("dp")
        user.save()
    return redirect('/')

@login_required(login_url="/changePassword/")
def changePassword(request):
    if request.method == "POST":
        data = request.POST
        user = get_object_or_404(CustomUser, username = request.user.username)
        old_password = data.get("old_password")
        if user.check_password(old_password) or user.isGuest == True:
            new_password = data.get("new_password")
            user.set_password(new_password)
            user.isGuest = False
            user.save()
        else:
            messages.error(request, "Invalid old password.")
            return redirect("/")

    return redirect('/')

def check_old_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        old_password = data.get('old_password')
        user = request.user
        if user.check_password(old_password):
            return JsonResponse({'valid': True})
        else:
            return JsonResponse({'valid': False})
    return JsonResponse({'valid': False}, status=400)

@login_required(login_url="/login/")
def home(request):
    usersInfo = CustomUser.objects.all()
    context = {'noIcons': range(50),
               'noSocialUser': range(200),
               'online': "green",
               'offline': "red",
               'name': "Aslam Miya",
               'username': "@aslammiya",
               'noOfUsers': 0,
               'usersInfo': usersInfo,
               'user': request.user
               }
    return render(request, "index.html", context)