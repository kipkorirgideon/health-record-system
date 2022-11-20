import django.forms

from records import models
from forms import FromMixin

BLANK_CHOICE = (('', '---'),)


class PatientCreateForm(FromMixin, django.forms.ModelForm):
    ward = django.forms.ChoiceField(choices=BLANK_CHOICE + models.Patient.WARD_CHOICES, label='Ward', required=True)

    class Meta:
        model = models.Patient
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'date_of_birth',
            'patient_id_number',
            'ward',
        )

    required_fields = (
        'first_name',
        'last_name',
        'date_of_birth',
        'patient_id_number',
        'ward',
    )


class PatientDoctorUpdateForm(FromMixin, django.forms.ModelForm):
    class Meta:
        model = models.PatientRecord
        fields = (
            'signs_and_symptoms',
            'test',
        )


class PatientLabTestUpdateForm(FromMixin, django.forms.ModelForm):
    class Meta:
        model = models.PatientRecord
        fields = (
            'test_result',
        )
