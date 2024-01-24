from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import UserProfile  # Подставьте свою модель пользователя
from django.contrib import messages
from django.contrib.auth import logout


def index(request):
    return render(request, 'finalapp/index.html')


def registration_popup(request):
    return render(request, 'finalapp/index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('finalapp/my_board.html')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'finalapp/my_board.html')


def logout_view(request):
    logout(request)
    return redirect('finalapp/index.html')


def my_board_view(request):
    return render(request, 'finalapp/my_board.html')


def profil_view(request):
    return render(request, 'finalapp/profil.html')


def shop_view(request):
    return render(request, 'finalapp/shop.html')


def achivments_view(request):
    return render(request, 'finalapp/achivments.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        english_level = request.POST.get('english-level')
        user = UserProfile(email=email, name=name, password=password, english_level=english_level)
        user.save()
        return redirect('my_board')
