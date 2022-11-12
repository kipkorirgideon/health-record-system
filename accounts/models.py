import uuid

import django
import model_utils.models
from django.db import models
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _

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
        user.save(using=self._db)
        return user


class User(django.contrib.auth.base_user.AbstractBaseUser, model_utils.models.TimeStampedModel,
           django.contrib.auth.models.PermissionsMixin):
    USER_DOCTOR = 'd'
    CASHIER = 'c'
    LAB_TECHNICIAN = 'l'
    PHARMACIST = 'p'
    USER_TYPE_CHOICES = (
        (USER_DOCTOR, 'Doctor'),
        (CASHIER, 'Cashier'),
        (LAB_TECHNICIAN, 'Lab Technician'),
        (PHARMACIST, 'Pharmacist'),
    )
    REQUIRED_FIELDS = ('first_name', 'last_name', 'user_type')
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = USERNAME_FIELD
    history = HistoricalRecords()
    first_name = models.CharField('First Name', max_length=50, blank=False, )
    last_name = models.CharField('Last Name', max_length=50, blank=False, )
    username = django.db.models.CharField(max_length=170, blank=True, default='')
    email = models.EmailField('Email', max_length=100, blank=False, unique=True, )
    is_active = django.db.models.BooleanField(_('active'), default=True)
    is_staff = django.db.models.BooleanField(_('admin'), default=False)
    user_type = models.CharField('User Type', max_length=1, choices=USER_TYPE_CHOICES, default=USER_DOCTOR, )
    id_number = models.CharField('ID Number', max_length=50, blank=False, unique=True, )

    objects = MainUserManager()

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
        ordering = ['first_name', 'last_name']
