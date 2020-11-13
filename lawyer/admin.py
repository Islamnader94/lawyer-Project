from django.contrib import admin
from django.contrib.auth.models import Permission
from lawyer.models import *

class RoleAdmin(admin.ModelAdmin):
    fields = ('value', 'account')

admin.site.register(BaseUser)
admin.site.register(Client)
admin.site.register(AccountUser)
admin.site.register(Admin)
admin.site.register(Contract)
admin.site.register(Case)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Expense)
admin.site.register(Task)
admin.site.register(Assignment)
admin.site.register(Account)
admin.site.register(Document)
admin.site.register(Permission)
admin.site.register(UserPermission)
admin.site.register(Payment)
admin.site.register(DocumentType)
admin.site.register(Message)
# admin.site.register(Role, RoleAdmin)
admin.site.register(Role)
