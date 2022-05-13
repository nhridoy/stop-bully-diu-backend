from rest_framework import serializers
from blog_app import models as blog_model


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog_model.BlogModel
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'slug': {'read_only': True},
        }
