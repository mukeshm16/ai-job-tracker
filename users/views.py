from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Register Page
def register_page(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create User
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/users/login/')

    return render(request, 'register.html')


# Login Page
def login_page(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/')

    return render(request, 'login.html')


# Logout
def logout_page(request):

    logout(request)

    return redirect('/users/login/')