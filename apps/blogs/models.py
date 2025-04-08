from django.db import models
from core.models import BaseModel


# Create your models here.
class Post(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_markdown = models.BooleanField(blank=True,null=True)
    
    def __str__(self):
        return self.title
