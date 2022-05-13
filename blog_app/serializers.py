from rest_framework import serializers
from blog_app import models as blog_model


class BlogTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog_model.BlogTagsModel
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog_model.BlogModel
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'slug': {'read_only': True},
        }


class ForumCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog_model.ForumCategoryModel
        fields = '__all__'


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog_model.ForumModel
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
        }
