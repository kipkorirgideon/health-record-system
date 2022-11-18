from django.urls import reverse_lazy
from django.views import generic

from . import forms
from . import models


# Create your views here.

class PatientCreateView(generic.CreateView):
    model = models.Patient
    form_class = forms.PatientCreateForm
    template_name = 'patient_create.html'
    success_url = reverse_lazy('home')


class PatientRecordUpdateView(generic.UpdateView):
    model = models.PatientRecord
    form_class = None
    template_name = 'patient_records_update.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'patient_uuid'

    def get_object(self, queryset=None):
        patient_uuid = self.kwargs.get('patient_uuid')
        patient = models.Patient.objects.get(uuid=patient_uuid)
        patient_record, created = self.model.objects.get_or_create(patient=patient)
        return patient_record


class PatientDoctorUpdateView(PatientRecordUpdateView):
    form_class = forms.PatientDoctorUpdateForm


class PatientLabTestUpdateView(PatientRecordUpdateView):
    form_class = forms.PatientLabTestUpdateForm


class PatientListView(generic.TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = self.request.user.user_type
        return context
