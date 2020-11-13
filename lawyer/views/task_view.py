import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from lawyer.serializers import task_serializer, assignment_serializer,\
    document_serializer, case_serializer
from lawyer.models import Task, Assignment,\
    ContentType, Message, Document
from lawyer.services import task_service


class TaskView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, task_id):
        task = Task.objects.filter(id=task_id)
        try:
            task = task[0]
            serializer = case_serializer.CaseSerializer(task)
            return JsonResponse(
                {'task': serializer.data}, 
                safe=False, 
                status=status.HTTP_200_OK
            )
        except ObjectDoesNotExist:
            message = Message.objects.get(code=404)
            return JsonResponse(
                {'error': message.message_en}, 
                safe=False, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception:
            message = Message.objects.get(code=500)
            return JsonResponse(
                {'error': message.message_en}, 
                safe=False, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ListTaskView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        tasks = Task.objects.values(
            'id',
            'task_title',
            'case_title',
            'contract_title',
            'assignment',
            'task_status',
            'due_date',
            'task_periority'
            )
        # serializer = contract_serializer.ContractSerializer(contracts, many=True)
        try:
            return JsonResponse(
                {'tasks': list(tasks)}, 
                safe=False, 
                status=status.HTTP_200_OK
            )
        except ObjectDoesNotExist:
            message = Message.objects.get(code=404)
            return JsonResponse(
                {'error': message.message_en}, 
                safe=False, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception:
            message = Message.objects.get(code=500)
            return JsonResponse(
                {'error': message.message_en}, 
                safe=False, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TaskAssignment(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, task_id):
        try:
            assignment = Assignment.objects.get(content_type__model__iexact="Task", object_id=task_id)
            serializer = assignment_serializer.AssignmentSerializer(assignment)
            return JsonResponse(
                {'assignment': serializer.data}, 
                safe=False, 
                status=status.HTTP_200_OK
            )
        except ObjectDoesNotExist:
            message = Message.objects.get(code=404)
            return JsonResponse(
                {'error': message.message_en}, 
                safe=False, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception:
            message = Message.objects.get(code=500)
            return JsonResponse(
                {'error': message.message_en}, 
                safe=False, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @csrf_exempt
    def post(self, request, task_id):
        payload = json.loads(request.body)
        try:
            assignment = task_service.task_assignment(task_id, payload)
            serializer = assignment_serializer.AssignmentSerializer(assignment)
            return JsonResponse(
                {'assignment': serializer.data},
                safe=False, 
                status=status.HTTP_201_CREATED
            )
        except ObjectDoesNotExist:
            message = Message.objects.get(code=404)
            return JsonResponse(
                {'error': message.message_en}, 
                safe=False, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception:
            message = Message.objects.get(code=500)
            return JsonResponse(
                {'error': message.message_en}, 
                safe=False, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TaskDocumentView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, task_id):
        try:
            document = Document.objects.get(content_type__model__iexact="Task", object_id=task_id)
            serializer = document_serializer.DocumentSerializer(document)
            return JsonResponse(
                {'document': serializer.data}, 
                safe=False, 
                status=status.HTTP_200_OK
            )
        except ObjectDoesNotExist:
            message = Message.objects.get(code=404)
            return JsonResponse(
                {'error': message.message_en}, 
                safe=False, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception:
            message = Message.objects.get(code=500)
            return JsonResponse(
                {'error': message.message_en}, 
                safe=False, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    @csrf_exempt
    def post(self, request, task_id):
        payload = json.loads(request.body)
        try:
            document = task_service.task_document(task_id, payload)
            serializer = document_serializer.DocumentSerializer(document)
            return JsonResponse(
                {'document': serializer.data},
                safe=False, 
                status=status.HTTP_201_CREATED
            )
        except ObjectDoesNotExist:
            message = Message.objects.get(code=404)
            return JsonResponse(
                {'error': message.message_en}, 
                safe=False, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception:
            message = Message.objects.get(code=500)
            return JsonResponse(
                {'error': message.message_en}, 
                safe=False, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )