from django.db import models
from user import models as user_model


# Create your models here.
class BlogModel(models.Model):
    user = models.ForeignKey(user_model.User, on_delete=models.CASCADE, related_name="user_blog")
    blogtitle = models.CharField(max_length=250, verbose_name="BLOG TITLE")
    blogcontent = models.TextField(verbose_name="BLOG CONTENT")
    blogimg = models.ImageField(upload_to="blog_image", verbose_name="ADD BLOG IMAGE", blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    published_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blogtitle


class ForumModel(models.Model):
    user = models.ForeignKey(user_model.User, on_delete=models.CASCADE, related_name="user_forum")
    title = models.CharField(max_length=250, verbose_name="Forum Title")
    content = models.TextField(verbose_name="Forum Content")
    slug = models.SlugField(max_length=250, unique=True)
    published_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ForumCommentModel(models.Model):
    forum_post = models.ForeignKey(ForumModel, on_delete=models.CASCADE, related_name='forum_post')
    user = models.ForeignKey(user_model.User, on_delete=models.CASCADE, related_name='user_forum_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ('-comment_date',)


class ForumLikesModel(models.Model):
    forum_post = models.ForeignKey(ForumModel, on_delete=models.CASCADE, related_name='forum_like')
    user = models.ForeignKey(user_model.User, on_delete=models.CASCADE, related_name='user_like')
