import django.forms

from records import models


class PatientCreateForm(django.forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'date_of_birth',
            'patient_id_number'
        )


class PatientDoctorUpdateForm(django.forms.ModelForm):
    class Meta:
        model = models.PatientRecord
        fields = (
            'signs_and_symptoms',
            'test',
        )
