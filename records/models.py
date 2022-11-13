from django.db import models
import model_utils.models


# Create your models here.

class Patient(model_utils.models.TimeStampedModel):
    first_name = models.CharField('First Name', max_length=50, blank=False, )
    last_name = models.CharField('Last Name', max_length=50, blank=False, )
    middle_name = models.CharField('Middle Name', max_length=50, blank=True, default='')
    date_of_birth = models.DateField('Date of Birth', blank=False, )
    patient_id_number = models.CharField('ID Number', max_length=50, blank=False, unique=True, )

    @property
    def is_active(self):
        if self.first_name:
            return True
        return False

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        ordering = ['first_name', 'last_name']


class PatientRecord(model_utils.models.TimeStampedModel):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='record')
    signs_and_symptoms = models.TextField('Signs and Symptoms', blank=True, default='')
    test = models.TextField('Diagnosis', blank=True, default='')
    test_result = models.TextField('Test Result', blank=True, default='')
    treatment = models.TextField('Treatment', blank=False, default='')

    def __str__(self):
        return f'{self.patient}'

    class Meta:
        verbose_name = 'Patient Record'
        verbose_name_plural = 'Patient Records'
        ordering = ['patient', 'created']
