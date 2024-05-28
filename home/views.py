from django.shortcuts import render

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

def loginUser(request):

    return render(request, "loginUser.html")

def userRegistration(request):

    return render(request, "userRegistration.html")