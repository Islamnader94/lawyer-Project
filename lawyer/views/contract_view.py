import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from lawyer.serializers import contract_serializer, assignment_serializer,\
    task_serializer, document_serializer
from lawyer.models import Contract, Assignment,\
    Payment, ContentType, Document, Message
from lawyer.services import contract_service


class ContractView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, contract_id):
        contract = Contract.objects.filter(id=contract_id)
        try:
            contract = contract[0]
            serializer = contract_serializer.ContractSerializer(contract)
            return JsonResponse(
                {'contract': serializer.data}, 
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
            contract = contract_service.add_contract(payload)
            serializer = contract_serializer.ContractSerializer(contract)
            return JsonResponse(
                {'contract': serializer.data}, 
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
    def put(self, request, contract_id):
        payload = json.loads(request.body)
        try:
            contract = contract_service.update_contract(contract_id, payload)
            serializer = contract_serializer.ContractSerializer(contract)
            return JsonResponse(
                {'contract': serializer.data}, 
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
    def delete(self, request, contract_id):
        try:
            contract = Contract.objects.get(id=contract_id)
            contract.delete()
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
                {'error': message.message_en}, 
                safe=False, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ListContractsView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        try:
            contracts = Contract.objects.values(
                'id',
                'contract_title',
                'status',
                'contract_stage',
                'contract_value',
                'client',
                'updated'
            )
            return JsonResponse(
                {'contracts': list(contracts)}, 
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


class ContractPaymentView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, contract_id):
        payment = Payment.objects.filter(contract=contract_id)
        payment = payment[0]
        try:
            serializer = contract_serializer.PaymentSerializer(payment)
            return JsonResponse(
                {'payment': serializer.data}, 
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
    def post(self, request, contract_id):
        payload = json.loads(request.body)
        try:
            payment = contract_service.contract_payment(contract_id, payload)
            serializer = contract_serializer.PaymentSerializer(payment)
            return JsonResponse(
                {'payment': serializer.data},
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


class ContractAssignmentView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, contract_id):
        try:
            assignment = Assignment.objects.get(content_type__model__iexact="Contract", object_id=contract_id)
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
    def post(self, request, contract_id):
        payload = json.loads(request.body)
        try:
            assignment = contract_service.contract_assignment(contract_id, payload)
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


class ContractTaskView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, contract_id):
        task = Task.objects.filter(object_id=contract_id)
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
    def post(self, request, contract_id):
        payload = json.loads(request.body)
        try:
            task = contract_service.contract_task(contract_id, payload)
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


class ContractDocumentView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, contract_id):
        try:
            import pdb;
            pdb.set_trace();
            document = Document.objects.get(content_type__model__iexact="Contract", object_id=contract_id)
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
    def post(self, request, contract_id):
        payload = json.loads(request.body)
        try:
            document = contract_service.contract_document(contract_id, payload)
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
