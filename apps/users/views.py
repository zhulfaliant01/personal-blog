from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        authenticate_user = authenticate(request, username=username, password=password)

        if not authenticate_user:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'auth/login.html')
        
        login(request, authenticate_user)
        return redirect('home')

class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')
    
    def post(self, request):
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Password doesn't match")
            return render(request, "auth/register.html")  

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return render(request, "auth/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, "auth/register.html")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request,user)
        messages.success(request, "Successfuly Register continue to Login.")
        return redirect("home")
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')