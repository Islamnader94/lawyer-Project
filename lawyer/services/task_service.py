from lawyer.models import Contract, Case,\
    ContentType, Task, AccountUser, BaseUser,\
    Assignment, Role, DocumentType, Document


def add_task(data):
    if data:
        user_email = data['created_by']
        account_user = BaseUser.objects.filter(email=user_email)
        if 'contract_title' in data:
            contract = Contract.objects.get(contract_title=data['contract_title'])
            case =  None
            data["created_by"] = account_user[0]
            data["updated_by"] = account_user[0]
            data["case_title"] = case
            data["contract_title"] = contract
            data["content_type"] = ContentType.objects.get_for_model(contract)
            data["object_id"] = contract.id
        else:
            case = Case.objects.get(case_title=data['case_title'])
            contract = None
            data["created_by"] = account_user[0]
            data["updated_by"] = account_user[0]
            data["case_title"] = case
            data["contract_title"] = contract
            data["content_type"] = ContentType.objects.get_for_model(case)
            data["object_id"] = case.id
        
        task = Task.objects.create(**data)
        return task
    else:
        return ('Something wrong happened!')


def update_task(task_id, data):
    if data:
        task_item = Task.objects.filter(id=task_id)
        task_item.update(**data)
        return task_item[0]
    else:
        return ('Something wrong happened!')


def task_assignment(task_id, data):
    if data:
        user_id = data['user']
        role_id = data['role']
        created_by_id = data['created_by']
        task = Task.objects.get(id=task_id)
        account_user = AccountUser.objects.filter(id=user_id)
        created_by_user = BaseUser.objects.filter(id=created_by_id)
        role = Role.objects.filter(group=role_id)
        data['created_by'] = created_by_user[0]
        data['updated_by'] = created_by_user[0]
        data['user'] = account_user[0]
        data['role'] = role[0]
        data["content_type"] = ContentType.objects.get_for_model(task)
        data["object_id"] = task.id
        assignment = Assignment.objects.create(**data)
        return assignment
    else:
        return ('Something wrong happened!')


def task_document(task_id, data):
    if data:
        created_by_id = data['created_by']
        document_type_id = data['document_type']
        task = Task.objects.get(id=task_id)
        created_by_user = BaseUser.objects.filter(id=created_by_id)
        document_type = DocumentType.objects.filter(id=document_type_id)
        data['created_by'] = created_by_user[0]
        data['updated_by'] = created_by_user[0]
        data['document_type'] = document_type[0]
        data['content_type'] = ContentType.objects.get_for_model(task)
        data['object_id'] = task.id
        document = Document.objects.create(**data)
        return document
    else:
        return ('Something wrong happened!')