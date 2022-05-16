from rest_framework import serializers
from e_shop import models as e_model


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = e_model.ProductsModel
        fields = '__all__'
        extra_kwargs = {
            'product_code': {'read_only': True}
        }
