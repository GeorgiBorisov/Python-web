from django.shortcuts import render, redirect
from python_web_exam.forms.post import PostsForm
from django.contrib.auth.models import User
from python_web_exam.models import Posts
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator

def create(request):
    if request.method == 'GET':
        session = Session.objects.get(session_key=request.session.session_key)
        user_id = session.get_decoded().get('_auth_user_id')
        form = PostsForm(initial={'author': user_id})
        data = {
            'title': 'Create post',
            'action': 'create',
            'form': form
        }
        return render(request, 'post.html', data)
    elif request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

def all_posts(request):
    if request.method == 'GET':
        post_list = Posts.objects.all().order_by('-created')
        paginator = Paginator(post_list, 5)
        page = request.GET.get('page', 1)
        posts = paginator.page(page)
        data = {
            'title': 'All posts',
            'posts': posts
        }
        data['custom_range'] = range(1,6)
        return render(request, 'list.html', data)
        
    
def single_post(request, pk):
    if request.method == 'GET':
        post = Posts.objects.get(pk=pk)
        author = User.objects.get(pk=post.author_id)
        print(request.user)
        data = {
            'title': post.title,
            'post': post,
            'author': author.username,
            'user': request.user
        }
        return render(request, 'singlePost.html', data)
    
def latest(request):
    if request.method == 'GET':
        posts = Posts.objects.all().order_by('-created')[:10]
        data = {
            'title': 'Latest',
            'posts': posts
        }
        return render(request, 'list.html', data)
    elif request.method == 'POST':
        form = EditPostsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('all-posts')
    
def edit_post(request, pk):
    post = Posts.objects.get(pk=pk)
    if request.method == 'GET':
        session = Session.objects.get(session_key=request.session.session_key)
        user_id = session.get_decoded().get('_auth_user_id')
        
        form = PostsForm(initial={
                'title': post.title,
                'content': post.content,
                'image': post.image,
                'author': user_id
            })
        data = {
            'title': post.title,
            'form': form,
            'action': 'edit',
            'id': post.pk,
        }
        return render(request, 'post.html', data)
    elif request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/post/' + str(post.pk))
        
def delete_post(request, pk):
    post = Posts.objects.get(pk=pk).delete()
    return redirect('all-posts')