from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Manager that helps to create user with validated credentials and hashed password"""

    def create_user(self, email, name, last_name, password=None):
        """Function that creates user"""
        if not email or not name or not last_name:
            raise ValueError('User must have correct credentials')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, last_name, password):
        """Function that creates admin user"""
        user = self.create_user(email, name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Database model that describes users in the system"""
    email = models.EmailField(max_length=30, unique=True, )
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='user/avatars/%y/%m/%d', blank=True,default='user/avatars/23/05/17/default.jpg')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False, editable=False)
    friends = models.ManyToManyField('self', blank=True, symmetrical=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name', 'password']

    def __str__(self):
        """" Return string representation of user to display it understandably in the admin panel """
        return self.email
