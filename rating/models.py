from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from BitBlog.base_manager import BaseManager
from accounts.models import CustomUser
from posts.models import Post


class Rating(models.Model):
    """
        microservice for rating posts
    """

    id = models.AutoField(db_column='ID', primary_key=True)
    is_reported = models.BooleanField(db_column='IsReported', default=False)
    is_accept = models.BooleanField(db_column='IsAccept', default=True)
    created_at = models.DateTimeField(db_column='Created', auto_now=True)
    updated_at = models.DateTimeField(db_column='Updated', auto_now_add=True)
    user_id = models.ForeignKey(CustomUser, db_column='User', on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, db_column='Post', on_delete=models.CASCADE)
    rate = models.IntegerField(
        db_column='Rate',
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        default=1,
        null=False,
        blank=False
    )

    objects = BaseManager()  # for exception handling.

    class Meta:
        ordering = ('-created_at',)
        db_table = 'Rating'

    def __str__(self):
        return f'{self.rate}'


@receiver(post_save, sender=Rating)
def update_increase(sender, instance, created, **kwargs):
    if created:
        post = instance.post_id
        post.rate_counter = F('rate_counter') + 1
        post.rate_sum = F('rate_sum') + instance.rate
        post.save()