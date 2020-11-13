from rest_framework import serializers
from lawyer.models import Reminder
from lawyer.serializers import task_serializer, user_serializer


class ReminderSerializer(serializers.ModelSerializer):
    task =  task_serializer.TaskSerializer(read_only=True)
    sender = user_serializer.BaseUserSerializer(read_only=True, many=True)
    receiver = user_serializer.BaseUserSerializer(read_only=True)
    class Meta:
        model = Reminder
        fields= '__all__'