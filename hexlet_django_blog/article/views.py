from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })


class ArticleSingleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        category = article.category
        return render(request, 'article/article_single.html', context={
            'article': article,
            'category': category
        })


class ArticleCreateView(View):
    template_name = 'article/create.html'

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('articles_index'))
        return render(request, self.template_name, {'form': form})


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
