from lawyer.models import Contract, AccountUser,\
    Role, ContentType, Assignment, Task,\
    Payment, BaseUser, DocumentType, Document


def add_contract(data):
    if data:
        user_email = data['created_by']
        account_user = AccountUser.objects.filter(email=user_email)
        data['created_by'] = account_user[0]
        data['updated_by'] = account_user[0]
        contract = Contract.objects.create(**data)
        return contract
    else:
        return ('Something wrong happened!')


def update_contract(contract_id, data):
    if data:
        contract_item = Contract.objects.filter(id=contract_id)
        contract_item.update(**data)
        return contract_item[0]
    else:
        return ('Something wrong happened!')


def contract_payment(contract_id, data):
    if data:
        created_by_id = data['created_by']
        contract = Contract.objects.get(id=contract_id)
        created_by_user = BaseUser.objects.filter(id=created_by_id)
        data['created_by'] = created_by_user[0]
        data['updated_by'] = created_by_user[0]
        data['contract'] = contract
        payment = Payment.objects.create(**data)
        return payment
    else:
        return ('Something wrong happened!')



def contract_document(contract_id, data):
    if data:
        created_by_id = data['created_by']
        document_type_id = data['document_type']
        contract = Contract.objects.get(id=contract_id)
        created_by_user = BaseUser.objects.filter(id=created_by_id)
        document_type = DocumentType.objects.filter(id=document_type_id)
        data['created_by'] = created_by_user[0]
        data['updated_by'] = created_by_user[0]
        data['document_type'] = document_type[0]
        data['content_type'] = ContentType.objects.get_for_model(contract)
        data['object_id'] = contract.id
        document = Document.objects.create(**data)
        return document
    else:
        return ('Something wrong happened!')


def contract_assignment(contract_id, data):
    if data:
        user_id = data['user']
        role_id = data['role']
        created_by_id = data['created_by']
        contract = Contract.objects.get(id=contract_id)
        account_user = AccountUser.objects.filter(id=user_id)
        created_by_user = BaseUser.objects.filter(id=created_by_id)
        role = Role.objects.filter(group=role_id)
        data['created_by'] = created_by_user[0]
        data['updated_by'] = created_by_user[0]
        data['user'] = account_user[0]
        data['role'] = role[0]
        data["content_type"] = ContentType.objects.get_for_model(contract)
        data["object_id"] = contract.id
        assignment = Assignment.objects.create(**data)
        return assignment
    else:
        return ('Something wrong happened!')


def contract_task(contract_id, data):
    if data:
        user_email = data['created_by']
        contract = Contract.objects.get(id=contract_id)
        account_user = AccountUser.objects.filter(email=user_email)
        data['created_by'] = account_user[0]
        data['updated_by'] = account_user[0]
        data['content_type'] = ContentType.objects.get_for_model(contract)
        data['object_id'] = contract.id
        task = Task.objects.create(**data)
        return task
    else:
        return ('Something wrong happened!')
