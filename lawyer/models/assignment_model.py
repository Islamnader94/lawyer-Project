from system.models import BaseModel, BaseLookUpModel
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Assignment(BaseModel):
    user = models.ForeignKey('lawyer.AccountUser', related_name='user', on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey('lawyer.Role', related_name='role', on_delete=models.CASCADE, null=True, blank=True)

    # Listed below are the mandatory fields for a generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    assignment_object = GenericForeignKey('content_type', 'object_id')