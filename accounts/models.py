from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import CustomUserManager


class CustomUser(AbstractUser):
    """
        A model for users with custom fields.
            For the convenience of the user,
            the user's email occurs with a
            password and password.
    """

    username = None
    email = models.EmailField(verbose_name='ایمیل', unique=True)
    first_name = models.CharField(verbose_name='نام', max_length=150, blank=True, null=True)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=150, blank=True, null=True)
    last_login = models.DateTimeField(verbose_name='آخرین ورود', blank=True, null=True)
    is_staff = models.BooleanField(
        verbose_name='کارمند',
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name='فعال',
        default=True,

    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'CustomUser'

    def __str__(self):
        return self.email
