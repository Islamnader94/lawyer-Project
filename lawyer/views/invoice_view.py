import json
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from lawyer.serializers import invoice_serializer
from lawyer.models import Invoice, Message, InvoiceItem
from lawyer.services import invoice_service


class InvoiceView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, invoice_id):
        try:
            invoice = Invoice.objects.filter(id=invoice_id)
            invoice = invoice[0]
            serializer = invoice_serializer.InvoiceSerializer(invoice)
            return JsonResponse(
                {'invoice': serializer.data}, 
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
            invoice = invoice_service.add_invoice(payload)
            serializer = invoice_serializer.InvoiceSerializer(invoice)
            return JsonResponse(
                {'invoice': serializer.data},
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
    def put(self, request, invoice_id):
        payload = json.loads(request.body)
        try:
            invoice = invoice_service.update_invoice(invoice_id, payload)
            serializer = invoice_serializer.InvoiceSerializer(invoice)
            return JsonResponse(
                {'invoice': serializer.data}, 
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
    def delete(self, request, invoice_id):
        try:
            invoice = Invoice.objects.get(id=invoice_id)
            invoice.delete()
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


class ListInvoicesView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        try:
            invoices = Invoice.objects.all()
            serializer = invoice_serializer.InvoiceSerializer(invoices, many=True)
            return JsonResponse(
                {'invoices': serializer.data}, 
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


class InvoiceItemView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        try:
            invoice_item = InvoiceItem.objects.all()
            invoice_item = invoice_item[0]
            serializer = invoice_serializer.InvoiceItemSerializer(invoice_item)
            return JsonResponse(
                {'invoice_item': serializer.data}, 
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
            invoice_item = invoice_service.add_invoice_item(payload)
            serializer = invoice_serializer.InvoiceSerializer(invoice_item)
            return JsonResponse(
                {'invoice_item': serializer.data},
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

