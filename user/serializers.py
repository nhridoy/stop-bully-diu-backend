from rest_framework import serializers, validators
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator

from user import models


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
        validators=[UnicodeUsernameValidator(), validators.UniqueValidator(queryset=models.User.objects.all())]
    )

    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True,
                                     validators=[validate_password])
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True,
                                      label='Retype Password')

    class Meta:
        model = models.User
        fields = ['username', 'email', 'full_name', 'phone_number', 'student_id', 'password', 'password2']

        extra_kwargs = {
            'full_name': {'required': True},
        }

    def validate(self, attrs):
        password = attrs.get('password')
        if attrs.get('username') == password:
            raise validators.ValidationError({'password': "username can not be your password"})
        if attrs.get('email') == password:
            raise validators.ValidationError({'password': "email can not be your password"})
        if attrs['password'] != attrs['password2']:
            raise validators.ValidationError({'password': "Password Doesn't Match"})
        if models.User.objects.filter(username=attrs['username']).exists():
            raise validators.ValidationError({'username': 'user with this User ID already exists.'})
        if models.User.objects.filter(student_id=attrs['student_id']).exists():
            raise validators.ValidationError({'student_id': 'user with this Student ID already exists.'})
        return super(NewUserSerializer, self).validate(attrs)

    def create(self, validated_data):
        user = models.User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            student_id=validated_data['student_id'],
            phone_number=validated_data['phone_number'],
            full_name=validated_data['full_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
