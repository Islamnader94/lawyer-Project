from system.models import BaseModel, BaseLookUpModel
from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from lawyer.models import assignment_model, document_model


class Task(BaseModel):
    ACTIVE, PENDING, DONE = 1, 2, 3
    class Periority(models.TextChoices):
        HIGH = "HIGH", "High"
        LOW = "LOW", "Low"
    contract_title = models.ForeignKey('lawyer.Contract', on_delete=models.CASCADE, null=True, blank=True)
    case_title = models.ForeignKey('lawyer.Case', on_delete=models.CASCADE, null=True, blank=True)
    task_title = models.CharField(max_length=40, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    due_date = models.DateField()
    task_description = models.TextField(max_length=300, null=True, blank=True)
    task_status = models.PositiveSmallIntegerField(choices=(
        (ACTIVE,'Active'),
        (PENDING,'Pending'),
        (DONE, 'Done')),
        default=1,
        null=True, 
        blank=True
    )
    task_periority = models.CharField(max_length=40, choices=Periority.choices, default=Periority.HIGH)
    assignment = GenericRelation(assignment_model.Assignment)
    document = GenericRelation(document_model.Document)

    # Listed below are the mandatory fields for a generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    task_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        app_label= 'lawyer'

        permissions = ( 
            ('manage_task', 'Who can manage and view list of tasks'),
        )


    def get_group_permissions(self):
        groups_id = list(self.roles.values_list('group',flat=True))
        permission_qs = Permission.objects.filter(group__in=groups_id)
        perms = permission_qs.values_list('lawyer', 'manage_task').order_by()
        return set("%s.%s" % (ct, name) for ct, name in perms)


    def has_role_perm(self, perm):
        return perm in self.get_group_permissions()


    def has_role_perms(self, perm_list, obj=None):
        """
        Returns True if the user has each of the specified permissions. If
        object is passed, it checks if the user has all required perms for this
        object.
        """
        return all(self.has_role_perm(perm) for perm in perm_list)