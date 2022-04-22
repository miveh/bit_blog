from django.db import models

# Don't Delete These Exception Imports
from .exceptions import *


class BaseManager(models.Manager):
    """
        Similar to `get_or_404` method, except that when
            you do not receive the object you
            can return a custom error.
    """

    def get_or_raise(self, *args, **kwargs):
        queryset = super().get_queryset()
        try:
            return queryset.get(*args, **kwargs)
        except queryset.model.DoesNotExist:
            raise eval(queryset.model._meta.object_name + 'DoesNotExistException')
