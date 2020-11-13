import jwt
from uuid import uuid4
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group,\
    PermissionsMixin, Permission
from django.utils import timezone
from lawyer.managers import CustomBaseUserManager
from system.models import BaseModel, BaseLookUpModel
from .document_model import Document


class UserPermission(BaseModel):
    name = models.CharField(max_length=100)
    permission = models.OneToOneField(Permission, on_delete=models.CASCADE)
    feature =  models.ForeignKey('lawyer.Feature', on_delete=models.CASCADE, null=True, blank=True)

    def  __str__(self):
        return self.permission.name


class Role(BaseLookUpModel):
    group = models.OneToOneField(Group, on_delete=models.SET_NULL, null=True, blank=True, unique=True)

    def __str__(self):
        return "{}".format(self.group.name)


class BaseUser(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        ACCOUNTUSER = "ACCOUNTUSER", "AccountUser"
        CLIENT = "CLIENT", "Client"

    type = models.CharField(max_length=40, choices=Types.choices, default=Types.ADMIN)
    email = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    mobile_number = models.CharField(max_length=40, null=True, blank=True)
    work_phone = models.CharField(max_length=40, null=True, blank=True)
    paci = models.CharField(max_length=40, null=True, blank=True)
    fax = models.CharField(max_length=6, null=True, blank=True)
    dob = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=40, null=True, blank=True)
    address2 = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    zip_code = models.CharField(max_length=6, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    notes = models.TextField(max_length=300, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    documents = GenericRelation(Document)
    account = models.ForeignKey(
        'lawyer.Account', 
        related_name='account', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)
    roles =  models.ManyToManyField(
        Role, 
        related_name="roles",
        blank=True
    )

    objects = CustomBaseUserManager()
    objects_with_deleted = CustomBaseUserManager(deleted=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().
        """
        return self._generate_jwt_token()


    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        set to 10 days
        """
        dt = datetime.now() + timedelta(days=10)

        token = jwt.encode({
            'token_type': "access",
            'user_id': self.pk,
            'exp': int(dt.strftime('%s')),
            "jti": uuid4().hex
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


    def get_group_permissions(self):
        groups_id = list(self.roles.values_list('group',flat=True))
        permission_qs = Permission.objects.filter(group__in=groups_id)
        if not permission_qs:
            return set()
        perms = permission_qs.values_list('content_type__app_label', 'codename').order_by()
        return set("%s.%s" % (ct, name) for ct, name in perms)


    def has_role_perm(self, perm):
        return perm in self.get_group_permissions()


    def has_role_perms(self, perm_list, obj=None):
        """
        Returns True if the user has each of the specified permissions. If
        object is passed, it checks if the user has all required perms for this
        object.
        """
        return all(self.has_role_perm(perm) for perm in perm_list)

    
    def delete(self, *args, **kwargs):
        self.deleted = True
        super().save(*args, **kwargs)


    def restore(self, *args, **kwargs):
        self.deleted = False
        super().save(*args, **kwargs)

    class Meta:
        app_label= 'lawyer'


class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=BaseUser.Types.ADMIN)


class AccountUserManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=BaseUser.Types.ACCOUNTUSER)


class ClientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=BaseUser.Types.CLIENT)


class Admin(BaseUser):
    objects = AdminManager()

    class Meta:
        proxy = True
        app_label = 'lawyer'


class AccountUser(BaseUser):
    objects = AccountUserManager()

    class Meta:
        proxy = True
        app_label = 'lawyer'


class Client(BaseUser):
    objects = ClientManager()

    class Meta:
        proxy = True
        app_label = 'lawyer'