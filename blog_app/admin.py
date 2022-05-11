from django.contrib import admin
from blog_app import models as blog_model

# Register your models here.
admin.site.register(blog_model.Category)
# admin.site.register(blog_model.SubCategory)
admin.site.register(blog_model.Blog)
admin.site.register(blog_model.BlogComment)
admin.site.register(blog_model.BlogLikes)
