from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from python_web_exam.forms.user import EditUserForm
from django.contrib.auth import authenticate, login, logout

def view_profile(request):
    if request.method == 'GET':
       user = User.objects.get(username=request.user)
       data = {
           'user': user,
           'action': 'view'
       }
       return render(request, 'profile.html', data)

def edit_profile(request):
    user = User.objects.get(username=request.user)
    if request.method == 'GET':
       form = EditUserForm()
       data = {
           'form': form,
           'action': 'edit'
       }
       return render(request, 'profile.html', data)
    elif request.method == 'POST':
        form = EditUserForm(request.POST)
        # print(form.errors.as_data)
        if form.is_valid():
            print(form)
            password = request.POST['new_password']
            confirm_password = request.POST['confirm_new_password']
            if password == confirm_password:
                username = request.POST['username']
                user.username = username
                user.password = password
                user.set_password(password)
                user.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                request.session['user_id'] = username
                request.session['is_logged'] = True
                return redirect('index')

def delete_profile(request):
    user = User.objects.get(username=request.user)
    user.delete()
    logout(request)
    return redirect('index')