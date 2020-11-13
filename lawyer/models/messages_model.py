# from system.models import BaseModel
from django.db import models


class Message(models.Model):
    code = models.CharField(max_length=200, null=True, blank=True)
    message_en = models.CharField(max_length=200, null=True, blank=True)
    messag_ar = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.code
