from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser # For login/logout

class UserModel(AbstractBaseUser): # Inheriting AbstractBaseUser Class
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    two_factor_authentication = models.BooleanField(default=False)
    USERNAME_FIELD = 'username' # To set what is to be used for login


    class Meta:
        verbose_name = "User"
        verbose_name_plural = 'Users'