from rest_framework import serializers
from lawyer.serializers import contract_serializer
from lawyer.models import Case, CourtType, CaseStage


class CourtTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtType
        fields = '__all__'


class CaseStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStage
        fields = '__all__'


class CaseSerializer(serializers.ModelSerializer):
    contract_type = contract_serializer.ContractSerializer(read_only=True)
    court_type = CourtTypeSerializer(read_only=True)
    case_stage = CaseStageSerializer(read_only=True)

    class Meta:
        model = Case
        fields = '__all__'