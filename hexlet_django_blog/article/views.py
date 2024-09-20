from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse


class ArticleView(View):
    def get(self, request, tags, article_id, *args, **kwargs):
        context = {
            'tags': tags,
            'article_id': article_id
        }
        return render(
            request, 'article/index.html', context=context
        )


def index(request, tags='python', article_id=42):
    url = reverse('article', args=(tags, article_id))
    return redirect(url)
