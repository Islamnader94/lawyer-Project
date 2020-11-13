from lawyer.models import Case, AccountUser,\
    Role, ContentType, Assignment,\
    Document, DocumentType, BaseUser


def add_case(data):
    if data:
        user_email = data['created_by']
        account_user = AccountUser.objects.filter(email=user_email)
        data['created_by'] = account_user[0]
        data['updated_by'] = account_user[0]
        case = Case.objects.create(**data)
        return case
    else:
        return ('Something wrong happened!')


def update_case(case_id, data):
    if data:
        case_item = Case.objects.filter(id=case_id)
        case_item.update(**data)
        return case_item[0]
    else:
        return ('Something wrong happened!')


def case_assignment(case_id, data):
    if data:
        user_id = data['user']
        role_id = data['role']
        case = Case.objects.get(id=case_id)
        account_user = AccountUser.objects.filter(id=user_id)
        role = Role.objects.filter(group=role_id)
        data['created_by'] = account_user[0]
        data['updated_by'] = account_user[0]
        data['user'] = account_user[0]
        data['role'] = role[0]
        data["content_type"] = ContentType.objects.get_for_model(case)
        data["object_id"] = case.id
        assignment = Assignment.objects.create(**data)
        return assignment
    else:
        return ('Something wrong happened!')


def case_document(case_id, data):
    if data:
        created_by_id = data['created_by']
        document_type_id = data['document_type']
        case = Case.objects.get(id=case_id)
        created_by_user = BaseUser.objects.filter(id=created_by_id)
        document_type = DocumentType.objects.filter(id=document_type_id)
        data['created_by'] = created_by_user[0]
        data['updated_by'] = created_by_user[0]
        data['document_type'] = document_type[0]
        data['content_type'] = ContentType.objects.get_for_model(case)
        data['object_id'] = case.id
        document = Document.objects.create(**data)
        return document
    else:
        return ('Something wrong happened!')


def case_task(case_id, data):
    if data:
        user_email = data['created_by']
        case = Case.objects.get(id=case_id)
        account_user = AccountUser.objects.filter(email=user_email)
        data['created_by'] = account_user[0]
        data['updated_by'] = account_user[0]
        data['content_type'] = ContentType.objects.get_for_model(case)
        data['object_id'] = case.id
        task = Task.objects.create(**data)
        return task
    else:
        return ('Something wrong happened!')
