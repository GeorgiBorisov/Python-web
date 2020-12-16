from django.shortcuts import render
from python_web_exam.models import Posts
from django.contrib.sessions.models import Session
from django.db.models import Q

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
            session = Session.objects.get(session_key=request.session.session_key)
            user_id = session.get_decoded().get('_auth_user_id')
            posts = Posts.objects.all().order_by('-created').filter(~Q(author=user_id))[:2]
            user_posts = Posts.objects.all().order_by('-created').filter(author=request.user)[:2]
            data = {
                'title': 'Home',
                'posts':posts,
                'user_posts':user_posts
            }
            return render(request, 'index.html', data)
            