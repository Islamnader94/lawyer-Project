from system.models import BaseModel, BaseLookUpModel
from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.fields import GenericRelation
from .assignment_model import Assignment
from .task_model import Task
from .document_model import Document


class CourtType(BaseLookUpModel):
    pass


class CaseStage(BaseLookUpModel):
    pass


class Case(BaseModel):
    case_title = models.CharField(max_length=40, null=True, blank=True)
    case_type = models.CharField(max_length=40, null=True, blank=True)
    contract = models.ForeignKey('lawyer.Contract', related_name='contract', on_delete=models.SET_NULL, null=True, blank=True)
    court_type = models.ForeignKey(CourtType, related_name='court_type', on_delete=models.SET_NULL, null=True, blank=True)
    contract_description = models.TextField(max_length=300, null=True, blank=True)
    case_stage = models.ForeignKey(CaseStage, related_name='case_stage', on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField()
    assignment = GenericRelation(Assignment)
    name = models.CharField(max_length=40, null=True, blank=True)
    mobile = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=40, null=True, blank=True)
    documents = GenericRelation(Document)
    tasks = GenericRelation(Task)

    class Meta:
        app_label = 'lawyer'


    def __str__(self):
        return self.case_title

    def get_group_permissions(self):
        groups_id = list(self.roles.values_list('group',flat=True))
        permission_qs = Permission.objects.filter(group__in=groups_id)
        perms = permission_qs.values_list('lawyer', 'manage_case').order_by()
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
