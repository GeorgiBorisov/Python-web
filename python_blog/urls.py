"""python_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from python_web_exam.views.index import index
from python_web_exam.views.auth import register, signin, signout
from python_web_exam.views.post import create, edit_post, single_post, delete_post, all_posts, latest, my_posts
from python_web_exam.views.profile import view_profile, edit_profile, delete_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout'),
    path('create/', create, name='create'),
    path('view-profile/', view_profile, name='view-profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
    path('delete-profile/', delete_profile, name='delete-profile'),
    path('all-posts/', all_posts, name='all-posts'),
    path('post/<int:pk>', single_post, name='single-post'),
    path('edit-post/<int:pk>', edit_post, name='edit-post'),
    path('delete-post/<int:pk>', delete_post, name='delete-post'),
    path('latest/', latest, name='latest'),
    path('my-posts/', my_posts, name='my-posts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

