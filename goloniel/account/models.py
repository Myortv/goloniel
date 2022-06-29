from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None ):
        if not email:
            raise ValueError('User must have an email!')

        user = self.model(
            email = self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
        )
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):

    password = models.CharField(_("password"), max_length=128)
    first_name = None
    last_name = None
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(null=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    content = models.TextField(null=True, blank=True)
    quote = models.CharField(max_length=250, null=True, blank=True)

    pictogram = models.ImageField(upload_to=f'pictograms/', blank=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return f' [{self.pk}]  {self.username}'
