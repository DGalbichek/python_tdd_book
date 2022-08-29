from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from superlists.settings import EMAIL_HOST_USER


class ListUserManager(BaseUserManager):
    def create_user(self, email):
        ListUser.objects.create(email=email)

    def create_superuser(self, email, password):
        self.create_user(email)


class ListUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email', 'height']
    objects = ListUserManager()

    @property
    def is_staff(self):
        return self.email == EMAIL_HOST_USER

    @property
    def is_active(self):
        return True


class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(max_length=255)