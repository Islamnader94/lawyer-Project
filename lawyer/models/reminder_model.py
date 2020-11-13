from django.db import models
from django.utils import timezone
from system.models import BaseModel


class Reminder(BaseModel):
    PENDING, INITATED, SENT = "Pending", "Initiated", "Sent"
    task = models.ForeignKey('lawyer.Task', related_name='task', on_delete=models.CASCADE, null=True, blank=True)
    sender =  models.ManyToManyField('lawyer.BaseUser', related_name='sender', blank=True)
    receiver = models.ForeignKey('lawyer.BaseUser', related_name='receiver', on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.CharField(max_length=40, null=True, blank=True)
    body = models.CharField(max_length=300, null=True, blank=True)
    sending_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=12, choices=((PENDING,'Pending'),(INITATED,'Initiated'),(SENT, 'Sent')), default='Paid', null=True, blank=True)

    class Meta:
        app_label = 'lawyer'
