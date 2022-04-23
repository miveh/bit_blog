from django.db import models
from BitBlog.base_manager import BaseManager
from accounts.models import CustomUser


class Post(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)
    title = models.CharField(max_length=50, db_column='Title', blank=False, null=False)
    body = models.TextField(max_length=200, db_column='Body', blank=False, null=False)
    rate_counter = models.IntegerField(db_column='RateCounter', blank=True, null=False, default=0) #zero means this post did not score
    rate_sum = models.IntegerField(db_column='RateSum', blank=True, null=False, default=0) #zero means this post did not score
    created_at = models.DateTimeField(auto_now_add=True, db_column='Created')
    updated_at = models.DateTimeField(auto_now=True, db_column='Updated')
    author = models.ForeignKey(CustomUser, db_column='Author', on_delete=models.CASCADE)

    objects = BaseManager()  # for exception handling

    class Meta:
        db_table = 'Post'

    @property
    def calculate_rate(self):
        if self.rate_counter == 0:
            return None
        return self.rate_sum / self.rate_counter

    def __str__(self):
        return self.title



