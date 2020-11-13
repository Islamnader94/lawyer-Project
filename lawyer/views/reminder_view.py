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
from lawyer.serializers import reminder_serializer
from lawyer.models import Reminder, Message
from lawyer.services import reminder_service


class ReminderView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, reminder_id):
        try:
            reminder = Reminder.objects.filter(id=reminder_id)
            reminder = reminder[0]
            serializer = reminder_serializer.ReminderSerializer(reminder)
            return JsonResponse(
                {'reminder': serializer.data}, 
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
            reminder = reminder_service.add_reminder(payload)
            serializer = reminder_serializer.ReminderSerializer(reminder)
            return JsonResponse(
                {'reminder': serializer.data}, 
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
    def put(self, request, reminder_id):
        payload = json.loads(request.body)
        try:
            reminder = reminder_service.update_reminder(reminder_id, payload)
            serializer = reminder_serializer.ReminderSerializer(reminder)
            return JsonResponse(
                {'reminder': serializer.data}, 
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
    def delete(self, request, reminder_id):
        try:
            reminder = Reminder.objects.get(id=reminder_id)
            reminder.delete()
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


class ListRemindersView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        try:
            reminders = Reminder.objects.all()
            serializer = reminder_serializer.ReminderSerializer(reminders, many=True)
            return JsonResponse(
                {'reminders': serializer.data}, 
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