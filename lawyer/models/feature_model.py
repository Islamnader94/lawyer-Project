from django.db import models
from system.models import BaseModel


class  Feature(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name