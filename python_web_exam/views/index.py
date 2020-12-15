from django.shortcuts import render
from python_web_exam.models import Posts

def index(request):
    if request.method == 'GET':
        if request.user == 'AnonymousUser':
            posts = Posts.objects.all().order_by('-created')[:4]
            data = {
                'title': 'Home',
                'posts':posts
            }
            return render(request, 'index.html', data)
        else:
            posts = Posts.objects.all().order_by('-created')[:2]
            user_posts = Posts.objects.all().order_by('-created').filter(author=request.user)[:2]
            data = {
                'title': 'Home',
                'posts':posts
            }
            return render(request, 'index.html', data)
            