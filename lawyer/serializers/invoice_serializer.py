from rest_framework import serializers
from lawyer.models import ItemType, Invoice, InvoiceItem
from lawyer.serializers import user_serializer, contract_serializer,\
    case_serializer


class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields= '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    customer_name = user_serializer.BaseUserSerializer(read_only=True)
    contract = contract_serializer.ContractSerializer(read_only=True)
    case = case_serializer.CaseSerializer(read_only=True)
    class Meta:
        model = Invoice
        fields= '__all__'


class InvoiceItemSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)
    item_type = ItemTypeSerializer(read_only=True)
    class Meta:
        model = InvoiceItem
        fields= '__all__'
