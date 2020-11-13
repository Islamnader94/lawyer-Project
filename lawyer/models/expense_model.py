from system.models import BaseModel, BaseLookUpModel
from django.db import models


class ExpensesType(BaseLookUpModel):
    pass

    class Meta:
        app_label = 'lawyer'


class Expense(BaseModel):
    expense_by = models.ForeignKey('lawyer.AccountUser', on_delete=models.CASCADE, null=True, blank=True)
    contract_title = models.ForeignKey('lawyer.Contract', on_delete=models.CASCADE, null=True, blank=True)
    case_title = models.ForeignKey('lawyer.Case', on_delete=models.CASCADE, null=True, blank=True)
    notes = models.TextField(max_length=300)
    expense_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    expense_date = models.DateField()

    class Meta:
        app_label = 'lawyer'


class ExpenseItem(BaseModel):
    expenece = models.ForeignKey(Expense, on_delete=models.CASCADE, null=True, blank=True)
    expence_type = models.ForeignKey(ExpensesType, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=40, null=True, blank=True)
    amount = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        app_label = 'lawyer'
