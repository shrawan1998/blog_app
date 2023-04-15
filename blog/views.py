from django.shortcuts import render

posts = [
    {
    'author': 'Narendra Singh',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'April 13, 2023'
    },
    {
    'author': 'Vineet',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'April 14, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'This is about page!'})