from django.shortcuts import render

def index(request):
    data = {
        'title': 'Home'
    }
    return render(request, 'index.html', data)