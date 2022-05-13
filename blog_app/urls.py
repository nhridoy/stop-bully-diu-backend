from django.urls import path
from blog_app import views as blog_view

urlpatterns = [
    path('blog_tags/', blog_view.BlogTagsView.as_view(), name="post_tags"),
    path('post/', blog_view.BlogPostView.as_view(), name="post_blog"),
    path('post_update/<id>/', blog_view.BlogPostUpdateView.as_view(), name="post_blog_update"),
    path('forum_post/', blog_view.ForumPostView.as_view(), name="forum_post_article"),
    path('forum_cat/', blog_view.ForumCategoriesView.as_view(), name="forum_categories"),
    path('forum_post/<id>/', blog_view.ForumPostUpdateView.as_view(), name="forum_update_article"),

]