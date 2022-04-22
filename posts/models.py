from django.db import models

from accounts.models import CustomUser


class Post(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)
    author = models.ForeignKey(CustomUser, db_column='Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, db_column='Title')
    body = models.TextField(max_length=200, db_column='Body')
    created_at = models.DateTimeField(auto_now_add=True, db_column='Created')
    updated_at = models.DateTimeField(auto_now=True, db_column='Updated')

    objects = BaseManager()

    class Meta:
        db_table = 'Post'

    def __str__(self):
        return self.title
