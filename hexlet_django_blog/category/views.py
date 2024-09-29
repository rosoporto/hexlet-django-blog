from django.shortcuts import render
from django.views import View
from hexlet_django_blog.category.models import Category


class IndexView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'category/index.html', context={
            'categories': categories,
        })
