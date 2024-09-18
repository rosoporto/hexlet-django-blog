from django.shortcuts import render
from django.views import View


class MainPageArticle(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'article/index.html', context={'who': 'article'}
        )
