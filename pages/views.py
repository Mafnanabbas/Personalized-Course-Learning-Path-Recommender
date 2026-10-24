from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def welcome(request):
    return render(request, 'index.html')
def create_account(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password') 

        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            
   
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login') 
            
        except Exception as e:
            messages.error(request, 'Error creating account. That email might already be in use.')
            
    return render(request, 'create_account.html')

def login_view(request):
    if request.method == 'POST':
        # Grab the email and password from form
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the user exists in Supabase
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Securely log them in
            login(request, user)
            # Redirect them to their personalized dashboard (we'll build this next!)
            return redirect('dashboard') 
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
            
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')