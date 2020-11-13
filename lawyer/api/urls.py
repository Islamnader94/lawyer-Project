from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from lawyer.views import user_view, task_view,\
  case_view, contract_view, expense_view,\
  reminder_view, invoice_view

urlpatterns = [
  #Token generator endpoints
  path('token', jwt_views.TokenObtainPairView.as_view(), name='token_generat'), # Payload email and password
  path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), #Payload refresh with old token value

  #Login user endpoint
  path('login', user_view.login),

  #Client urls
  path('client', user_view.ClientView.as_view()),
  path('client/<int:client_id>', user_view.ClientView.as_view()),
  path('client/<int:client_id>/document', user_view.ClientDocumentView.as_view()),
  path('list-clients', user_view.ClientListView.as_view()),

  #Account user urls
  path('account-user', user_view.AccountUserView.as_view()),
  path('account-user/<int:user_id>', user_view.AccountUserView.as_view()),
  path('list-users', user_view.AccountUserListView.as_view()),

  #Case urls
  path('list-cases', case_view.ListCasesView.as_view()),
  path('case', case_view.CaseView.as_view()),
  path('case/<int:case_id>', case_view.CaseView.as_view()),
  path('case/<int:case_id>/assignment', case_view.CaseAssignment.as_view()),
  path('case/<int:case_id>/task', case_view.CaseTask.as_view()),
  path('case/<int:case_id>/document', case_view.CaseDocumentView.as_view()),

  #Contract urls
  path('list-contracts', contract_view.ListContractsView.as_view()),
  path('contract', contract_view.ContractView.as_view()),
  path('contract/<int:contract_id>', contract_view.ContractView.as_view()),
  path('contract/<int:contract_id>/payment', contract_view.ContractPaymentView.as_view()),
  path('contract/<int:contract_id>/assignment', contract_view.ContractAssignmentView.as_view()),
  path('contract/<int:contract_id>/task', contract_view.ContractTaskView.as_view()),
  path('contract/<int:contract_id>/document', contract_view.ContractDocumentView.as_view()),

  #Invoice urls
  path('list-invoices', invoice_view.ListInvoicesView.as_view()),
  path('invoice', invoice_view.InvoiceView.as_view()),
  path('invoice/<int:invoice_id>', invoice_view.InvoiceView.as_view()),
  path('invoice-item', invoice_view.InvoiceItemView.as_view()),

  # Expense urls
  path('list-expenses', expense_view.ListExpensesView.as_view()),
  path('expense', expense_view.ExpenseView.as_view()),
  path('expense/<int:expense_id>', expense_view.ExpenseView.as_view()),
  path('expense-item', expense_view.ExpensesItemView.as_view()),

  # Reminder urls
  path('list-reminders', reminder_view.ListRemindersView.as_view()),
  path('reminder', reminder_view.ReminderView.as_view()),
  path('reminder/<int:reminder_id>', reminder_view.ReminderView.as_view()),

  #Task  urls
  path('list-tasks', task_view.ListTaskView.as_view()),
  path('task/<int:task_id>', task_view.TaskView.as_view()),
  path('task/<int:task_id>/assignment', task_view.TaskAssignment.as_view()),
  path('task/<int:task_id>/document', task_view.TaskDocumentView.as_view()),
]