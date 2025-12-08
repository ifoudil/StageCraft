from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def connexion(request) :
    user = None

    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        return render(
            request,
            'applistagecraft/test.html',
            {"user": user}
        )
    
    usr = request.POST['username']
    pwd = request.POST['password']
    user = authenticate (request, username = usr, password = pwd)
    if user is not None :
        login(request, user)
        return render(
            request,
            'applistagecraft/test.html',
            {"user": user}
        )

    else :
        return render(
            request,
            'applicompte/login.html'
        )


def deconnexion(request):
    user = None

    if request.user.is_authenticated:
        logout(request)
        return render(
            request,
            'applicompte/logout.html'
        )
    
    else :
        return render(
            request,
            'applicompte/login.html'
        )
