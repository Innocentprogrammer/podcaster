import requests
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "index.html")

def landing(request):
    return render(request,"index1.html")

def signup(request):

    if request.method=="POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        myuser=User.objects.create_user(username, email, password1)
        myuser.first_name=fname
        myuser.last_name=lname
        
        myuser.save()

        messages.success(request, "Your account has been created successfully")
        
        return redirect("signin")

    return render(request,"signup.html")

def signin(request):

    if request.method =="POST":
        username = request.POST.get("username")
        password1=request.POST.get("password1")

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request,user)
            return redirect("landing")
            
        else:
            messages.error(request,"Bad Credentials")
            return redirect("home")

    return render(request,"signin.html")

def signout(request):
    logout(request)
    messages.success(request,"logged out Successfully")
    return redirect('home')

def google_login(request):
    google_auth_url = "https://accounts.google.com/o/oauth2/auth"
    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
    }
    request_url = f"{google_auth_url}?{'&'.join([f'{key}={value}' for key, value in params.items()])}"
    return redirect(request_url)

def google_callback(request):
    if "code" not in request.GET:
        return redirect("home")  # Redirect to home if authentication fails

    code = request.GET["code"]
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
        "code": code,
    }

    # Exchange authorization code for an access token
    token_response = requests.post(token_url, data=data)
    token_data = token_response.json()
    access_token = token_data.get("access_token")

    if not access_token:
        return redirect("home")

    # Get user info
    user_info_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    user_info_response = requests.get(user_info_url, headers=headers)
    user_info = user_info_response.json()

    email = user_info.get("email")
    name = user_info.get("name")

    # Check if user exists, else create one
    user, created = User.objects.get_or_create(username=email, defaults={"first_name": name, "email": email})

    # Log in the user
    login(request, user)

    return redirect("landing")
