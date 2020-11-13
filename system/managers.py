from django.db import models


class BaseModelManager(models.Manager):
  def __init__(self, *args, **kwargs):
    self.with_deleted = kwargs.pop('deleted', False)
    super(BaseModelManager, self).__init__(*args, **kwargs)

  def _base_queryset(self):
    return super().get_queryset().filter()

  def get_queryset(self):
    qs = self._base_queryset()
    if self.with_deleted:
      return qs.filter(deleted=True)
    return qs.filter(deleted=False)