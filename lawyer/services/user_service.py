from django.contrib.auth.hashers import make_password
from lawyer.models import Client, BaseUser,\
    AccountUser, Document, DocumentType, ContentType


def add_client(data):
    if data:
        data['type'] = BaseUser.Types.CLIENT
        data['password'] = make_password(data['password'])
        client = Client.objects.create(**data)
        return client
    else:
        return ('Something wrong happened!')


def update_client(client_id, data):
    if data:
        client_item = Client.objects.filter(id=client_id)
        client_item.update(**data)
        return client_item[0]
    else:
        return ('Something wrong happened!')


def client_document(client_id, data):
    if data:
        created_by_id = data['created_by']
        document_type_id = data['document_type']
        client = Client.objects.get(id=client_id)
        created_by_user = BaseUser.objects.filter(id=created_by_id)
        document_type = DocumentType.objects.filter(id=document_type_id)
        data['created_by'] = created_by_user[0]
        data['updated_by'] = created_by_user[0]
        data['document_type'] = document_type[0]
        data['content_type'] = ContentType.objects.get_for_model(client)
        data['object_id'] = client.id
        document = Document.objects.create(**data)
        return document
    else:
        return ('Something wrong happened!')


def add_account_user(data):
    if data:
        data['type'] = BaseUser.Types.ACCOUNTUSER
        data['password'] = make_password(data['password'])
        user = AccountUser.objects.create(**data)
        return user
    else:
        return ('Something wrong happened!')


def update_account_user(user_id, data):
    if data:
        user_item = AccountUser.objects.filter(id=user_id)
        user_item.update(**data)
        return user_item[0]
    else:
        return ('Something wrong happened!')