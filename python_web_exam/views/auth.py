from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from python_web_exam.forms.user import UsersForm, UsersLoginForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django import forms

def register(request):
    if request.method == 'GET':
        form = UsersForm()
        data = {
            'form': form,
            'action': 'register',
            'title': 'Register'
        }
        return render(request, 'auth.html', data)
    elif request.method == 'POST':
        form = UsersForm(request.POST)
        print(form.is_valid())
        print(form.errors.as_data)
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if form.is_valid() and password == confirm_password:
           
            if password == confirm_password:
                user = form.save(commit=False)
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user.set_password(password)
                user.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                request.session['user_id'] = username
                request.session['is_logged'] = True
                return redirect('index')
        else:
            if password != confirm_password:
                form.add_error('confirm_password', 'Passowrds do not match')
            data = {
            'form': form,
            'action': 'register',
            'title': 'Register'
            }
            return render(request, 'auth.html', data)
            
def signin(request):
    if request.method == 'GET':
        form = UsersLoginForm()
        data = {
            'form': form,
            'action': 'login',
            'title': 'Login'
        }
        return render(request, 'auth.html', data)
    elif request.method == 'POST':
        form = UsersLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session['user_id'] = username
                request.session['is_logged'] = True
                print('here I am')
                login(request,user)
                data = {
                    'user': username
                }
                return redirect('index')
            else:
                if not User.objects.filter(username=username).exists():
                    form.add_error('username', 'Non existing username')
                if User.objects.filter(username=username).exists():
                    form.add_error('password', 'The password is incorrect')
                data = {
                    'form': form,
                    'action': 'login',
                    'title': 'Login'
                }
                return render(request, 'auth.html', data)
            
def signout(request):
    logout(request)
    print(request)
    return redirect('index')