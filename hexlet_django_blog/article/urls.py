from django.urls import path
from hexlet_django_blog.article import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:id>/edit/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('<int:id>/', views.ArticleSingleView.as_view(), name='article_single'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('redirect_exp/', views.redirect_example, name='redirect_exp'),
    path('<str:tags>/<int:article_id>/', views.ArticleView.as_view(), name='article'),
    path('redirect_in_url', RedirectView.as_view(pattern_name='articles_index', permanent=True)),
]
