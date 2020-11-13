from lawyer.models import Expense, ExpenseItem



def add_expense(data):
    if data:
        expense = Expense.objects.create(**data)
        return expense
    else:
        return ('Something wrong happened!')


def add_expense_item(data):
    if data:
        expense_id = data['expense']
        expense = Expense.objects.filter(id=expense_id)
        data['expense'] = expense[0]
        expense_item = ExpenseItem.objects.create(**data)
        return expense_item
    else:
        return ('Something wrong happened!')


def update_expense(expense_id, data):
    if data:
        expense_item = Expense.objects.filter(id=expense_id)
        expense_item.update(**data)
        return expense_item[0]
    else:
        return ('Something wrong happened!')