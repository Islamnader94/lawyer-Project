from rest_framework import serializers
from generic_relations.relations import GenericRelatedField
from lawyer.serializers import task_serializer, user_serializer,\
    case_serializer, contract_serializer
from lawyer.models import Assignment, Role,\
    Task, Case, Contract


class AssignmentSerializer(serializers.ModelSerializer):
    user = user_serializer.BaseUserSerializer(read_only=True)
    role = user_serializer.RoleSerializer(read_only=True)
    assignment_object = GenericRelatedField({
        Task: task_serializer.TaskSerializer(),
        Case: case_serializer.CaseSerializer(),
        Contract: contract_serializer.ContractSerializer()
    })

    class Meta:
        model = Assignment
        fields = '__all__'