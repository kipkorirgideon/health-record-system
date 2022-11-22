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
    signs_and_symptoms = django.forms.CharField(widget=django.forms.Textarea(attrs={'rows': 4, }),
                                                required=True, label='Signs and Symptoms',
                                                help_text='Add signs and symptoms')
    test = django.forms.CharField(widget=django.forms.Textarea(attrs={'rows': 4, }),
                                  required=True, label='Diagnosis', help_text='Add lab test to be done')

    class Meta:
        model = models.PatientRecord
        fields = (
            'signs_and_symptoms',
            'test',
        )

    required_fields = (
        'signs_and_symptoms',
        'test',
    )


class PatientLabTestUpdateForm(FromMixin, django.forms.ModelForm):
    test_result = django.forms.CharField(widget=django.forms.Textarea(attrs={'rows': 4, }),
                                         required=True, label='Test Result', help_text='Add lab test result')

    class Meta:
        model = models.PatientRecord
        fields = (
            'test_result',
        )

    required_fields = (
        'test_result',
    )


class PatientTreatmentUpdateForm(FromMixin, django.forms.ModelForm):
    treatment = django.forms.CharField(widget=django.forms.Textarea(attrs={'rows': 4, }),
                                       required=True, label='Treatment', help_text='Add treatment')

    class Meta:
        model = models.PatientRecord
        fields = (
            'treatment',
        )

    required_fields = (
        'treatment',
    )
