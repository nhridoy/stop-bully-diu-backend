from django.db import models
from user import models as user_model


# Create your models here.
class BlogTagsModel(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class BlogModel(models.Model):
    user = models.ForeignKey(user_model.User, on_delete=models.CASCADE, related_name="user_blog")
    blogtitle = models.CharField(max_length=250)
    blogcontent = models.TextField()
    blogimg = models.ImageField(upload_to="blog_image", blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    tags = models.ManyToManyField(BlogTagsModel, related_name='blog_tags', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blogtitle


class ForumCategoryModel(models.Model):
    category = models.CharField(max_length=100)


class ForumModel(models.Model):
    user = models.ForeignKey(user_model.User, on_delete=models.CASCADE, related_name="user_forum")
    categories = models.ManyToManyField(ForumCategoryModel, blank=True, null=True, related_name="user_forum_categories")
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


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
