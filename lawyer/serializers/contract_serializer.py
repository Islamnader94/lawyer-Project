from rest_framework import serializers
from lawyer.models import ContractStage, ContractType,\
    Contract, Payment
from lawyer.serializers import user_serializer


class ContractStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractStage
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class ContractTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractType
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    contract_type = ContractTypeSerializer(read_only=True)
    contract_stage = ContractStageSerializer(read_only=True)
    client = user_serializer.BaseUserSerializer(read_only=True)
    class Meta:
        model = Contract
        fields = '__all__'