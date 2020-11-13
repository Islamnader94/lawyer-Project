from rest_framework import serializers
from lawyer.models import Document, DocumentType,\
    Case, Contract, Task, Client
from lawyer.serializers import case_serializer, contract_serializer,\
    task_serializer, user_serializer
from generic_relations.relations import GenericRelatedField


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    document_type = DocumentTypeSerializer(read_only=True)
    document_object = GenericRelatedField({
        Task: task_serializer.TaskSerializer(),
        Case: case_serializer.CaseSerializer(),
        Contract: contract_serializer.ContractSerializer(),
        Client: user_serializer.ClientSerializer(),
    })

    class Meta:
        model = Document
        fields = '__all__'