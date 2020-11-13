from rest_framework import serializers
from lawyer.models import ExpensesType, Expense, ExpenseItem
from lawyer.serializers import user_serializer, contract_serializer,\
    case_serializer


class ExpensesTypeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ExpensesType
        fields= '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    expense_by = user_serializer.BaseUserSerializer(read_only=True)
    contract = contract_serializer.ContractSerializer(read_only=True)
    case = case_serializer.CaseSerializer(read_only=True)
    class Meta:
        model = Expense
        fields= '__all__'


class ExpenseItemSerializer(serializers.ModelSerializer):
    expense = ExpenseSerializer(read_only=True)
    expense_type = ExpensesTypeSerializer(read_only=True)
    class Meta:
        model = ExpenseItem
        fields= '__all__'