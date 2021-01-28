from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 27, 2018'
    },
    {
        'author': 'Chafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 26, 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')