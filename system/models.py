from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords
from django_currentuser.middleware import get_current_user,\
    get_current_authenticated_user
from system.managers import BaseModelManager


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name="created_%(app_label)s_%(class)s",
        on_delete=models.SET_NULL
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name="updated_%(app_label)s_%(class)s",
        on_delete=models.SET_NULL
    )
    history = HistoricalRecords(inherit=True)

    objects = BaseModelManager()
    objects_with_deleted = BaseModelManager(deleted=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.created_by = get_current_authenticated_user()
        self.updated_by = get_current_authenticated_user()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.pk is None:
            self.created_by = get_current_authenticated_user()
        self.updated_by = get_current_authenticated_user()
        self.deleted = True
        super().save(*args, **kwargs)

    def restore(self, *args, **kwargs):
        if self.pk is None:
            self.created_by = get_current_authenticated_user()
        self.updated_by = get_current_authenticated_user()
        self.deleted = False
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class BaseLookUpModel(models.Model):
    account = models.ForeignKey('lawyer.Account', on_delete=models.CASCADE, null=True, blank=True)
    value = models.CharField(max_length=40, null=True, blank=True)
    class Meta:
        abstract = True

    def __str__(self):
        return str(self.account)