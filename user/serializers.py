from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from rest_framework import validators
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from . import models


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # info = serializers.CharField(source='permission_user')
    non_field_errors = {
        'detail': 'Please verify your mail.'
    }
    default_error_messages = {
        'detail': 'Username or Password does not matched.'
    }

    def validate(self, attrs):
        # print(attrs)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # print(data)
        if self.user.is_active:
            request = self.context.get('request')

            obj = {
                'id': self.user.id,
                'email': self.user.email,
                'is_staff': self.user.is_staff,
                'is_active': self.user.is_active,
            }

            data.update({'user': obj})
            return data

        else:
            msg = "Your account is not active"

        raise serializers.ValidationError({'detail': msg})


class NewUserSerializer(serializers.ModelSerializer):
    """
    New User Registration Serializer
    """
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=models.User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UnicodeUsernameValidator()]
    )

    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True,
                                     validators=[validate_password])
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True,
                                      label='Retype Password')

    class Meta:
        model = models.User
        fields = ['username', 'email', 'full_name', 'password', 'password2']

        extra_kwargs = {
            'full_name': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise validators.ValidationError({'password': "Password Doesn't Match"})
        if models.User.objects.filter(username=attrs['username']).exists():
            raise validators.ValidationError({'username': 'user with this User ID already exists.'})
        return attrs

    def create(self, validated_data):
        user = models.User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            full_name=validated_data['full_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
