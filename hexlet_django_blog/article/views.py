from django.shortcuts import render


def index(request):
    return render(
        request, 'article/index.html', context={'who': 'article'}
    )
