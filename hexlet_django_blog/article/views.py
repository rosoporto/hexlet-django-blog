from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from hexlet_django_blog.article.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })


class ArticleView(View):
    def get(self, request, tags, article_id, *args, **kwargs):
        context = {
            'tags': tags,
            'article_id': article_id
        }
        return render(
            request, 'article/exp_rederict.html', context=context
        )


def redirect_example(request, tags='python', article_id=42):
    url = reverse('article', args=(tags, article_id))
    return redirect(url)
