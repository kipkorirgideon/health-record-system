import uuid
from django.db import models
import model_utils.models
from native_shortuuid import NativeShortUUIDField


# Create your models here.

class Patient(model_utils.models.TimeStampedModel):

    YEARS_CATEGORY = (
        ('10-15', '10-15'),
        ('15-20', '15-20'),
        ('20-25', '20-25'),
        ('25-30', '25-30'),
        ('30-35', '30-35'),
        ('35-40', '35-40'),
        ('40-45', '40-45'),
        ('45+', '45+'),
    )

    KAKUMA_WARD = 'Kakuma Ward'
    LAPUR_WARD = 'Lapur Ward'
    LETE_WARD = 'Lete Ward'
    SONGOT_WARD = 'Songot Ward'
    KALOBEYEI_WARD = 'Kalobeyei Ward'
    LOKICHOGIO = 'Lokichogio'
    NANAAM_WARD = 'Nanaam Ward'

    WARD_CHOICES = (
        (KAKUMA_WARD, 'Kakuma Ward'),
        (LAPUR_WARD, 'Lapur Ward'),
        (LETE_WARD, 'Lete Ward'),
        (SONGOT_WARD, 'Songot Ward'),
        (KALOBEYEI_WARD, 'Kalobeyei Ward'),
        (LOKICHOGIO, 'Lokichogio'),
        (NANAAM_WARD, 'Nanaam Ward'),
    )

    uuid = NativeShortUUIDField(editable=False, unique=True, default=uuid.uuid4)
    first_name = models.CharField('First Name', max_length=50, blank=False, )
    last_name = models.CharField('Last Name', max_length=50, blank=False, )
    middle_name = models.CharField('Middle Name', max_length=50, blank=True, default='')
    date_of_birth = models.DateField('Date of Birth', blank=False, )
    patient_id_number = models.CharField('ID Number', max_length=50, blank=False, null=False, unique=True, )
    ward = models.CharField('Ward', max_length=50, choices=WARD_CHOICES, blank=False, default='')

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        ordering = ['first_name', 'last_name']

    
    @property
    def is_active(self):
        if self.first_name:
            return True
        return False

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # number of years since birth
    def age(self):
        import datetime
        today = datetime.date.today()
        AGE = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        if AGE < 10:
            return '10 and below'
        elif AGE > 10 and AGE < 15:
            return '10-15'
        elif AGE > 15 and AGE < 20:
            return '15-20'
        elif AGE > 20 and AGE < 25:
            return '20-25'
        elif AGE > 25 and AGE < 30:
            return '25-30'
        elif AGE > 30 and AGE < 35:
            return '30-35'
        elif AGE > 35 and AGE < 40:
            return '35-40'
        elif AGE > 40 and AGE < 45:
            return '40-45'
        elif AGE > 45:
            return '45 and above'

class PatientRecord(model_utils.models.TimeStampedModel):
    uuid = NativeShortUUIDField(editable=False, unique=True, default=uuid.uuid4)
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
