from system.models import BaseModel, BaseLookUpModel
from django.db import models


#should belookup for contract, expenses or services
class ItemType(BaseLookUpModel):
    pass


class Invoice(BaseModel):
    UNPAID, PAID = 'Unpaid','Paid'

    customer_name = models.ForeignKey('lawyer.Client', on_delete=models.CASCADE, null=True, blank=True)
    contract = models.ForeignKey('lawyer.Contract', on_delete=models.CASCADE, null=True, blank=True)
    case = models.ForeignKey('lawyer.Case', on_delete=models.CASCADE, null=True, blank=True)
    invoice_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    invoice_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=12, choices=((UNPAID,'Unpaid'), (PAID,'Paid')), default='Paid', null=True, blank=True)
    customer_note = models.TextField(max_length=300, null=True, blank=True)
    individual_note = models.TextField(max_length=300, null=True, blank=True)

    class Meta:
        app_label = 'lawyer'


class InvoiceItem(BaseModel):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=40, null=True, blank=True)
    amount = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        app_label = 'lawyer'
