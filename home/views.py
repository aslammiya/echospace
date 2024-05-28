from django.shortcuts import render

def home(request):
    context = {'noIcons': range(15),
               'noSocialUser': range(20),
               'online': "green",
               'offline': "red"
               }
    return render(request, "index.html", context)

def profile(request):
    context = {'name': "Aslam Miya",
               'username': "aslammiya",
               }
    return render(request, "profile.html", context)