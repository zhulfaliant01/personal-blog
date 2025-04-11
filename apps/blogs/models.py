from django.db import models
from django.contrib.auth import get_user_model

from core.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        get_user_model(),  # this ensures it works even if you use a custom User model
        on_delete=models.CASCADE,
        related_name="posts"
    )
    is_markdown = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.title