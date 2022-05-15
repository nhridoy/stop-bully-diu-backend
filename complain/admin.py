from django.contrib import admin
from complain import models as complain_model

# Register your models here.
admin.site.register(complain_model.ComplainModel)
