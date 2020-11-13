from django.dispatch import receiver
from django.db.models.signals import post_save
from lawyer.models import UserPermission, Role, ContentType
from django.contrib.auth.models import Permission, Group

@receiver(post_save, sender=UserPermission)
def auto_create_Permission(sender, instance, created, **kwargs):
    if created:
        Permission.objects.get_or_create(
            name = instance.name,
            content_type = ContentType.objects.get_for_model(UserPermission),
            codename = instance.name
        )


@receiver(post_save, sender=Role)
def auto_create_Group(sender, instance, created, **kwargs):
    import pdb;
    pdb.set_trace();
    if created:
        Group.objects.get_or_create(
            name = f'{instance.value}  {str(instance.id)}'
        )