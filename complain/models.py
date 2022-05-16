from django.db import models
from user import models as user_model

# Create your models here.
status = (
    ('new', 'New'),
    ('processing', 'Processing'),
    ('closed', 'Closed'),
)


class ComplainModel(models.Model):
    user = models.ForeignKey(user_model.User, on_delete=models.CASCADE, related_name='complain_user')
    location = models.CharField(max_length=255, blank=True)
    suspect = models.CharField(max_length=255, blank=True)
    suspect_description = models.CharField(max_length=255, blank=True)
    details = models.TextField()
    attachments = models.FileField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=status)
    complain_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.details
