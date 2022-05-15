from rest_framework import serializers
from complain import models as complain_model


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = complain_model.ComplainModel
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }


class ComplainStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = complain_model.ComplainModel
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'attachments': {'read_only': True},
            'details': {'read_only': True},
            'location': {'read_only': True},
        }
