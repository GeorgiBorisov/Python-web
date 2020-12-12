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
       form = EditUserForm(initial={'username':user.username})
       data = {
           'title': 'Edit profile',
           'form': form,
           'action': 'edit'
       }
       return render(request, 'profile.html', data)
    elif request.method == 'POST':
        print(request.POST)
        form = EditUserForm(request.POST)
        current_password = request.POST['current_password']
        username = request.POST['username']
        user = authenticate(request, username=username, password=current_password)
        password = request.POST['new_password']
        confirm_password = request.POST['confirm_new_password']
        if form.is_valid() and password == confirm_password and user is not None:
            user.username = username
            user.password = password
            user.set_password(password)
            user.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            request.session['user_id'] = username
            request.session['is_logged'] = True
            return redirect('index')
        else:
            data = {
                'title': 'Edit profile',
                'form': form,
                'action': 'edit'
            }
            if password != confirm_password:
                form.add_error('confirm_new_password', 'Passowrds do not match')
            if user == None:
                form.add_error('current_password', 'Incorrect password or username')
            return render(request, 'profile.html', data)               
            

def delete_profile(request):
    user = User.objects.get(username=request.user)
    user.delete()
    logout(request)
    return redirect('index')