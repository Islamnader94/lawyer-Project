import json
from django.utils import timezone
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from permissions import CustomPermissions
from lawyer.services import user_service
from lawyer.serializers import user_serializer, document_serializer
from lawyer.models import Client, Admin,\
    AccountUser, BaseUser, Document, Message


@api_view(["POST"])
@csrf_exempt
def login(request):
    """
    Function to handle login request
    """
    payload = json.loads(request.body)
    try:
        email = payload['email']
        password = payload['password']
        user = authenticate(username=email, password=password)
        user_type = user.type

        #checking user's type
        if user_type == 'ADMIN':
            serializer = user_serializer.AdminSerializer(user)
        elif user_type == 'ACCOUNTUSER':
            serializer = user_serializer.AccountUserSerializer(user)
        else:
            serializer = user_serializer.ClientSerializer(user)

        #return user with token
        if user:
            user.last_login = timezone.now()
            user.save()
            data = {
                'token': user.token,
                'user_data': serializer.data
            }
            return JsonResponse(
                {'user': data}, 
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


class AccountUserView(APIView):
    permission_classes = [IsAuthenticated, CustomPermissions]
    permission_required = ["lawyer.view_accountuser"]

    @csrf_exempt
    def get(self, request, user_id):
        """
        Function to get account user
        """
        try:
            user = AccountUser.objects.filter(id=user_id).values(
                'id',
                'first_name',
                'last_name',
                'mobile_number',
                'roles'
            )
            user = user[0]
            return JsonResponse(
                {'user': user}, 
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
        """
        Function to add new account user
        """
        payload = json.loads(request.body)
        try:
            user = user_service.add_account_user(payload)
            serializer = user_serializer.AccountUserSerializer(user)
            return JsonResponse(
                {'user': serializer.data}, 
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
    def put(self, request, user_id):
        """
        Function to update requested account user
        """
        payload = json.loads(request.body)
        try:
            user = user_service.update_account_user(user_id, payload)
            serializer = user_serializer.AccountUserSerializer(user)
            return JsonResponse(
                {'user': serializer.data},
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


class AccountUserListView(APIView):
    permission_classes = [IsAuthenticated, CustomPermissions]
    permission_required = ["lawyer.view_accountuser"]

    @csrf_exempt
    def get(self, request):
        try:
            users = AccountUser.objects.all()
            serializer = user_serializer.AccountUserSerializer(users, many=True)
            return JsonResponse(
                {'users': serializer.data},
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


class ClientView(APIView):
    permission_classes = [IsAuthenticated, CustomPermissions]
    permission_required = ["lawyer.view_client"]

    @csrf_exempt
    def get(self, request, client_id):
        try:
            client = Client.objects.filter(id=client_id).values(
                'id',
                'first_name',
                'last_name',
                'email'
            )
            client = client[0]
            return JsonResponse(
                {'client': client}, 
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
        """
        Function to add new clients
        """
        payload = json.loads(request.body)
        try:
            client = user_service.add_client(payload)
            serializer = user_serializer.ClientSerializer(client)
            return JsonResponse(
                {'client': serializer.data}, 
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
    def put(self, request, client_id):
        """
        Function to update requested client
        """
        payload = json.loads(request.body)
        try:
            client = user_service.update_client(client_id, payload)
            serializer = user_serializer.ClientSerializer(client)
            return JsonResponse(
                {'client': serializer.data},
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


class ClientListView(APIView):
    permission_classes = [IsAuthenticated, CustomPermissions]
    permission_required = ["lawyer.view_client"]

    @csrf_exempt
    def get(self, request):
        clients = Client.objects.values(
            'id',
            'first_name',
            'last_name',
            'email',
            'mobile_number'
        )
        # serializer = user_serializer.ClientSerializer(clients, many=True)
        return JsonResponse(
            {'clients': list(clients)}, 
            safe=False, 
            status=status.HTTP_200_OK
        )


class ClientDocumentView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request, client_id):
        try:
            document = Document.objects.get(content_type__model__iexact="Document", object_id=client_id)
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
    def post(self, request, client_id):
        payload = json.loads(request.body)
        try:
            document = user_service.client_document(client_id, payload)
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