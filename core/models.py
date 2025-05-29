from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
import os

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class SocialPlatform(models.Model):
    platform_name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.platform_name  
class PartnerOrganization(models.Model):
    org_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="uya/partners/logos/", blank=True, null=True)  
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)  

    def __str__(self):
        return self.org_name
    
class ActivityPhoto(models.Model):
    image = models.ImageField(upload_to="uya/activities/")
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.caption and self.image:
            self.caption = os.path.basename(self.image.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.caption