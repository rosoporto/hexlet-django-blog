from django.urls import path
from hexlet_django_blog.article.views import ArticleView, IndexView, redirect_example


urlpatterns = [
    path('', IndexView.as_view(), name='article_index'),
    path('redirect_exp/', redirect_example, name='redirect_exp'),
    path('articles/<str:tags>/<int:article_id>/', ArticleView.as_view(), name='article'),
]
