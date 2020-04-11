from django.urls import path
from . import views


urlpatterns = [
    path('categories/<slug:category_slug>/', views.CategoryView.as_view(), name="category"),
    path('posts/<slug:post_slug>/', views.PostView.as_view(), name="post"),
    path('', views.HomeView.as_view()),


]
