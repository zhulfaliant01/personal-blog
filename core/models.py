from bson import ObjectId
from django.db import models


def generate_object_id():
    return str(ObjectId())


# Create your models here.
class BaseModel(models.Model):
    id = models.CharField(
        primary_key=True, max_length=24, default=generate_object_id, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # To make inform django to not create a table for this object/model
    class Meta:
        abstract = True
