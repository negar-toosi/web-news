from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.base_user import BaseUserManager as BUM
from django.contrib.auth import get_user_model
class BaseUserManager(BUM):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(('The Email must be set'))
        if not password:
            raise ValueError(('The password must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractUser): 
    username = models.CharField(max_length=10,null=True)
    email = models.EmailField(unique=True) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = BaseUserManager()
    
    def __str__(self):
        return self.email
    


class Author(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True, related_name='author')
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    phone = models.CharField(max_length=11, null=True)
    EMPLOYMENT_STATUS = models.CharField(max_length=20, choices=[
        ('processing','processing'),
        ('accepted','accepted'),
    ],blank=True)
    education = models.CharField(max_length=225,null=True)
    biography = models.TextField(null=True)
    # salary = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/',blank=True,null=True)

    