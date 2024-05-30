from django.shortcuts import render, redirect
from .models import customeUser

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
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        profile_picture = request.FILES.get('profile_picture')

        if all([first_name, last_name, username, password, profile_picture]):
            user = customeUser.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                profile_picture=profile_picture
            )
            return redirect('sign_in')
        else:
            # Handle invalid form submission
            context = {'error': 'Please fill in all fields.'}
            return render(request, 'userRegistration.html', context)
    else:
        return render(request, 'userRegistration.html')

def sign_in(request):

    return render(request, "loginUser.html")


def sign_out(request):
    pass