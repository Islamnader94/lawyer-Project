from django.db import models
from system.models import BaseModel, BaseLookUpModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class DocumentType(BaseLookUpModel):
    pass


class Document(BaseModel):
    name = models.CharField(max_length=40, null=True, blank=True)
    type = models.ForeignKey(DocumentType, related_name='document_type', on_delete=models.CASCADE, null=True, blank=True)
    file_upload = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)

    # Listed below are the mandatory fields for a generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    document_object = GenericForeignKey('content_type', 'object_id')
