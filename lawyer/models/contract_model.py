from system.models import BaseModel, BaseLookUpModel
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from .document_model import Document
from .assignment_model import Assignment


class ContractStage(BaseLookUpModel):
    pass


class ContractType(BaseLookUpModel):
    pass


class Contract(BaseModel):
    OPEN, CLOSED = 1,2
    contract_title = models.CharField(max_length=40, null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=((OPEN,'Open'),(CLOSED,'Closed')), default=1, null=True, blank=True)
    contract_type = models.ForeignKey(ContractType, on_delete=models.SET_NULL, null=True, blank=True )
    contract_description = models.TextField(max_length=300, null=True, blank=True)
    client = models.ForeignKey('lawyer.Client', related_name='client', on_delete=models.CASCADE, null=True, blank=True)
    contract_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    fee = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    contract_stage = models.ForeignKey(ContractStage, related_name='contract_stage', on_delete=models.SET_NULL, null=True, blank=True)
    assignment = GenericRelation(Assignment)
    documents = GenericRelation(Document)

    class Meta:
        app_label = 'lawyer'

    def __str__(self):
        return self.contract_title


class Payment(BaseModel):
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    due_date = models.DateField()
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.amount