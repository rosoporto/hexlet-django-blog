from django.urls import path
from hexlet_django_blog.category import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='categories_index'),
    path('<int:id>/', views.CategorySingleView.as_view(), name='category_single'),
    path('create/', views.CategoryCreateView.as_view(), name='category_create'),
]
