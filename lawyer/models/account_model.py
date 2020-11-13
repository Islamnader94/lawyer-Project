from django.db import models
from system.models import BaseModel


class Account(BaseModel): #when created, by default create 6 role using signals
    name = models.CharField(max_length=50, unique=True,  null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    contact_person = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'lawyer'