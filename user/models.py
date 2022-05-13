from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import FileExtensionValidator


# Create your models here.

class UserManager(BaseUserManager):
    """
    This is the manager for custom user model
    """

    def create_user(self, username, email, full_name, student_id, password=None):

        if not username:
            raise ValueError('Username should not be empty')
        if not email:
            raise ValueError('Email should not be empty')
        if not full_name:
            raise ValueError('Name should not be empty')
        if not student_id:
            raise ValueError('Student ID should not be empty')
        if not password:
            raise ValueError('Password should not be empty')

        user = self.model(
            username=username,
            email=self.normalize_email(email=email),
            full_name=full_name,
            student_id=student_id,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, full_name, student_id, password=None):
        user = self.create_user(
            username=username, email=email, full_name=full_name, student_id=student_id, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model Class
    """
    username = models.CharField(
        max_length=100, verbose_name='Username', unique=True, blank=False)
    email = models.EmailField(
        max_length=100, verbose_name='Email', unique=True, blank=True)
    full_name = models.CharField(verbose_name='Full Name', max_length=100)
    phone_number = models.CharField(max_length=255, verbose_name="Phone Number")

    date_joined = models.DateTimeField(
        verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    gender_options = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    student_id = models.CharField(max_length=100, unique=True, blank=False)

    is_staff = models.BooleanField(verbose_name='Staff Status', default=False, help_text='Designate if the user has '
                                                                                         'staff status')
    is_active = models.BooleanField(verbose_name='Active Status', default=True, help_text='Designate if the user has '
                                                                                          'active status')
    is_superuser = models.BooleanField(verbose_name='Superuser Status', default=False, help_text='Designate if the '
                                                                                                 'user has superuser '
                                                                                                 'status')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'username', 'student_id']

    objects = UserManager()

    def __str__(self):
        return self.full_name



