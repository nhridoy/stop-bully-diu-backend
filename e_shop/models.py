from django.db import models
import uuid

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProductsModel(models.Model):
    product_name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255, unique=True, blank=True, null=True)
    product_price = models.FloatField(blank=True, null=True)
    product_desc = models.TextField(blank=True)
    product_stock = models.IntegerField(blank=True)


@receiver(post_save, sender=ProductsModel, dispatch_uid="product_add")
def update_product_code(sender, instance, created, **kwargs):
    if created:
        product_id = uuid.uuid4()
        print(instance.product_name.replace(' ', ''))
        instance.product_code = f"{instance.product_name.replace(' ', '')}{(str(product_id)).split('-').pop()}"
        instance.save()
