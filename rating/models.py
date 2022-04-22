from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from BitBlog import settings
from posts.models import Post


class CommentAndRating(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='User', on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, db_column='Food', on_delete=models.CASCADE)
    is_reported = models.BooleanField(db_column='IsReported', default=False)
    is_accept = models.BooleanField(db_column='IsAccept', default=True)
    created_at = models.DateTimeField(db_column='Created', auto_now=True)
    updated_at = models.DateTimeField(db_column='Updated', auto_now_add=True)
    rate = models.IntegerField(
        db_column='Rate',
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        default=1,
        null=False,
        blank=False
    )

    objects = BaseManager()

    class Meta:
        ordering = ('-created',)
        db_table = 'Rating'
        # unique_together = ['post_id', 'user_id']

    def __str__(self):
        return f'{self.rate}'
