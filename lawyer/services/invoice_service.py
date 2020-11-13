from lawyer.models import Client, Contract,\
    Case, Invoice, BaseUser, InvoiceItem

def add_invoice(data):
    if data:
        created_by_id = data['created_by']
        case_id = data['case']
        contract_id = data['contract']
        client_id = data['customer_name']
        user = BaseUser.objects.filter(id=created_by_id)
        client = Client.objects.filter(id=client_id)
        contract = Contract.objects.filter(id=contract_id)
        case = Case.objects.filter(id=case_id)
        data['created_by'] = user[0]
        data['updated_by'] = user[0]
        data['customer_name'] = client[0]
        data['contract'] = contract[0]
        data['case'] = case[0]
        invoice = Invoice.objects.create(**data)
        return invoice
    else:
        return ('Something wrong happened!')


def add_invoice_item(data):
    if data:
        invoice_id = data['invoice']
        invoice = Invoice.objects.filter(id=invoice_id)
        data['invoice'] = invoice[0]
        invoice_item = InvoiceItem.objects.create(**data)
        return invoice_item
    else:
        return ('Something wrong happened!')



def update_invoice(invoice_id, data):
    if data:
        invoice = Invoice.objects.filter(id=invoice_id)
        invoice.update(**data)
        return invoice[0]
    else:
        return ('Something wrong happened!')