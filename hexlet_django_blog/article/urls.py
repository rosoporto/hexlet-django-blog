from django.urls import path
from hexlet_django_blog.article.views import MainPageArticle


urlpatterns = [
    path('', MainPageArticle.as_view(), name='article_index'),
]