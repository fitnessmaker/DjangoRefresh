from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        username  = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user already taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email exist")
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name)
                user.save()
                print("user created")
                return redirect("login")

        else:
            messages.info(request,"Password does not match")
        return redirect("register")

    else:
        
        return render(request,"register.html")
    


def login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.info(request,"User successfully Logedin")
            return redirect("/")
        else:
            messages.error(request,"Check Credentials")
            return redirect("login")
    else:
        return render(request,"login.html")
    

def logout(request):

    auth.logout(request)
    messages.info(request,"Logout Success")

    return redirect("/")






