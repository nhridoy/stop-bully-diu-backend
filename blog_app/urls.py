from django.urls import path
from blog_app import views as blog_view

urlpatterns = [
    path('post/', blog_view.BlogPostView.as_view(), name="post_blog"),


]