import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from lawyer.serializers import case_serializer, assignment_serializer,\
    task_serializer, document_serializer
from lawyer.models import Case, Assignment,\
    Task, ContentType, Document, Message
from lawyer.services import case_service


class CaseView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, case_id):
        try:
            case = Case.objects.filter(id=case_id)
            case = case[0]
            serializer = case_serializer.CaseSerializer(case)
            return JsonResponse(
                {'case': serializer.data}, 
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
    def post(self, request):
        payload = json.loads(request.body)
        try:
            case = case_service.add_case(payload)
            serializer = case_serializer.CaseSerializer(case)
            return JsonResponse(
                {'case': serializer.data}, 
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


    @csrf_exempt
    def put(self, request, case_id):
        payload = json.loads(request.body)
        try:
            case = case_service.update_case(case_id, payload)
            serializer = case_serializer.CaseSerializer(case)
            return JsonResponse(
                {'case': serializer.data}, 
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
    def delete(self, request, case_id):
        try:
            case = Case.objects.get(id=case_id)
            case.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
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
                {'error': message.messag_en}, 
                safe=False, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ListCasesView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        cases = Case.objects.values(
            'id',
            'case_title',
            'case_type',
            'case_stage',
            'updated'
        )
        # serializer = case_serializer.CaseSerializer(cases, many=True)
        try:              
            return JsonResponse(
                {'cases': list(cases)}, 
                safe=False, 
                status=status.HTTP_200_OK
            )
        except ObjectDoesNotExist:
            message = Message.objects.get(code=404)
            return JsonResponse(
                {'error': message.messag_en}, 
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


class CaseDocumentView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, case_id):
        try:
            document = Document.objects.get(content_type__model__iexact="Case", object_id=case_id)
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
    def post(self, request, case_id):
        payload = json.loads(request.body)
        try:
            document = case_service.case_document(case_id, payload)
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


class CaseAssignment(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, case_id):
        try:
            assignment = Assignment.objects.get(content_type__model__iexact="Case", object_id=case_id)
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
    def post(self, request, case_id):
        payload = json.loads(request.body)
        try:
            assignment = case_service.case_assignment(case_id, payload)
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

       
class CaseTask(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, case_id):
        task = Task.objects.filter(object_id=case_id)
        task = task[0]
        try:
            serializer = task_serializer.TaskSerializer(task)
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


    @csrf_exempt
    def post(self, request, case_id):
        payload = json.loads(request.body)
        try:
            task = case_service.case_task(case_id, payload)
            serializer = task_serializer.TaskSerializer(task)
            return JsonResponse(
                {'task': serializer.data},
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
