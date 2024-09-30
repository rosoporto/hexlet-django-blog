from django.shortcuts import render, get_object_or_404
from django.views import View
from hexlet_django_blog.category.models import Category


class IndexView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'category/index.html', context={
            'categories': categories,
        })


class CategorySingleView(View):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs['id'])
        articles_category = category.articles.all()  # article_set
        return render(request, 'category/category_single.html', context={
            'category': category,
            'articles_category': articles_category
        })
