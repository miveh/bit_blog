from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import CustomUserManager


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    username = None
    email = models.EmailField(verbose_name='ایمیل', unique=True)
    first_name = models.CharField(verbose_name='نام', max_length=150, blank=True)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=150, blank=True)
    is_staff = models.BooleanField(
        verbose_name='کارمند',
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name='فعال',
        default=True,

    )
    last_login = models.DateTimeField(verbose_name='آخرین ورود', blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
