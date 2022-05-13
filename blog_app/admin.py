from django.contrib import admin
from blog_app import models as blog_model

# Register your models here.
admin.site.register(blog_model.BlogModel)
admin.site.register(blog_model.ForumModel)
admin.site.register(blog_model.ForumCommentModel)
admin.site.register(blog_model.ForumLikesModel)
