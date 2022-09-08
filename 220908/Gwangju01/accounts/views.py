from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.urls import is_valid_path
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request) :
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST' :
        form = AuthenticationForm(request, request.POST)
        if form.is_valid() :
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else :
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request) :
    auth_logout(request)
    return redirect("articles:index")

def signup(request) :
    if request.method == 'POST' :
        form = CustomUserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else :
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

def delete(request) :
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

def update(request) :
    if request.method == 'POST' :
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid() :
            form.save()
            return redirect('articles:index')

    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

def change_password(request) :
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else :
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)