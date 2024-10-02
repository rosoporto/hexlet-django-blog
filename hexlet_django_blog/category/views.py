from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from hexlet_django_blog.category.models import Category
from hexlet_django_blog.category.forms import CategoryForm


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


class CategoryCreateView(View):
    template_name = 'category/category_create.html'

    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        return render(request, self.template_name, context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('categories_index'))
        return render(request, self.template_name, {'form': form})
