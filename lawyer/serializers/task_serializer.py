from rest_framework import serializers
from generic_relations.relations import GenericRelatedField
from lawyer.models import Task, Case,Contract, Document
from lawyer.serializers import case_serializer, contract_serializer



class TaskSerializer(serializers.ModelSerializer):
    contract_title = contract_serializer.ContractSerializer(read_only=True)
    case_title = case_serializer.CaseSerializer(read_only=True)
    task_object = GenericRelatedField({
        Case: case_serializer.CaseSerializer(),
        Contract: contract_serializer.ContractSerializer()
    })

    class Meta:
        model = Task
        fields = '__all__'