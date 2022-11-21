import uuid

import django
import model_utils.models
from django.db import models
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
from native_shortuuid import NativeShortUUIDField

from simple_history.models import HistoricalRecords


# Create your models here.

class MainUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(django.contrib.auth.base_user.AbstractBaseUser, model_utils.models.TimeStampedModel,
           django.contrib.auth.models.PermissionsMixin):
    USER_TYPE_DOCTOR = 'd'
    USER_TYPE_CASHIER = 'c'
    USER_TYPE_LAB_TECHNICIAN = 'l'
    USER_TYPE_PHARMACIST = 'p'
    USER_TYPE_CHOICES = (
        (USER_TYPE_DOCTOR, _('Doctor')),
        (USER_TYPE_CASHIER, _('Cashier')),
        (USER_TYPE_LAB_TECHNICIAN, _('Lab Technician')),
        (USER_TYPE_PHARMACIST, _('Pharmacist')),
    )
    REQUIRED_FIELDS = ()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = USERNAME_FIELD
    history = HistoricalRecords()
    uuid = NativeShortUUIDField(editable=False, unique=True, default=uuid.uuid4)
    first_name = models.CharField('First Name', max_length=50, blank=False, )
    last_name = models.CharField('Last Name', max_length=50, blank=False, )
    username = models.CharField(max_length=170, blank=True, default='')
    email = models.EmailField('Email', max_length=100, blank=False, unique=True, )
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('admin'), default=False)
    user_type = models.CharField('User Type', max_length=1, choices=USER_TYPE_CHOICES, blank=False, null=False,)

    objects = MainUserManager()

    def clean(self):
        print('user_type', self.user_type)
        super().clean()
        if not self.user_type:
            raise django.core.exceptions.ValidationError('User Type is required')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def user_name(self):
        return self.username if self.username else self.first_name

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
