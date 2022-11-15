from django.shortcuts import render

posts_list = [
    {
        'author': 'Roberto',
        'title': 'Blog Post 1 Test',
        'content': 'First post content here',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Roberto Kozako',
        'title': 'Blog Post 2 Test',
        'content': 'Second post content here',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts_list
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
