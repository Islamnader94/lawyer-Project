from rest_framework import serializers
from lawyer.models import BaseUser, Account,\
    Client, AccountUser, Admin, Role


class AccountSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name']


class BaseUserSerializer(serializers.ModelSerializer):
    account = AccountSerialzer(read_only=True)
    class Meta:
        model = BaseUser
        fields = [
            'id',
            'type', 
            'first_name', 
            'email', 
            'last_name', 
            'mobile_number', 
            'work_phone',
            'paci',
            'fax',
            'dob',
            'address',
            'address2',
            'city',
            'zip_code',
            'country',
            'notes',
            'account',
            'is_staff',
            'is_active',
            'date_joined',
            'last_login'
        ]


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = [
            'id',
            'type', 
            'first_name', 
            'email', 
            'last_name', 
            'mobile_number', 
            'work_phone',
            'paci',
            'fax',
            'dob',
            'address',
            'address2',
            'city',
            'zip_code',
            'country',
            'notes',
            'account',
            'is_staff',
            'is_active',
            'date_joined',
            'last_login',
            'deleted'
        ]


class AccountUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountUser
        fields = [
            'id',
            'type', 
            'first_name', 
            'email', 
            'last_name', 
            'mobile_number', 
            'work_phone',
            'paci',
            'fax',
            'dob',
            'address',
            'address2',
            'city',
            'zip_code',
            'country',
            'notes',
            'account',
            'is_staff',
            'is_active',
            'date_joined',
            'last_login',
            'deleted'
        ]


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'