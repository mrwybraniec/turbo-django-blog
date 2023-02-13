import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Application `Post` object reflecting `post` in the database."""

    author: int = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title: str = models.CharField(max_length=200)
    text: str = models.TextField()
    created_date: datetime.datetime = models.DateTimeField(default=timezone.now)
    published_date: datetime.datetime = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """This methods saves the post in the database."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.title
