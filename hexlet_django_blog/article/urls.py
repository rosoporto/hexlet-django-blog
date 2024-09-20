from django.urls import path
from hexlet_django_blog.article.views import ArticleView, index


urlpatterns = [
    path('', index, name='article_index'),
    path('articles/<str:tags>/<int:article_id>/', ArticleView.as_view(), name='article'),
]
