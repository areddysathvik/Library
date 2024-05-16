from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from books.models import Book

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('login') 
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('account_home')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def account_home(request):
    books = Book.objects.all()
    user_info = None
    if request.user.is_authenticated:
        user_info = {
            'username': request.user.username,
            'borrowed_books': request.user.borrowed_books.all(),
            'late_fee': request.user.late_fee,
        }
    
    return render(request, 'homepage.html', {'books': books, 'user_info': user_info})
