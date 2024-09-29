from django.urls import path
from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:id>/', views.ArticleSingleView.as_view(), name='article_single'),
    path('redirect_exp/', views.redirect_example, name='redirect_exp'),
    path('articles/<str:tags>/<int:article_id>/', views.ArticleView.as_view(), name='article'),
]
