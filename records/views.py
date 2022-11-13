from django.urls import reverse_lazy
from django.views import generic

from records.forms import PatientCreateForm, PatientDoctorUpdateForm
from . import models


# Create your views here.

class PatientCreateView(generic.CreateView):
    model = models.Patient
    form_class = PatientCreateForm
    template_name = 'patient_create.html'
    success_url = reverse_lazy('home')


class PatientDoctorUpdateView(generic.UpdateView):
    model = models.PatientRecord
    form_class = PatientDoctorUpdateForm
    template_name = 'patient_doctor_update.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'patient_id'

    def get_object(self, queryset=None):
        patient_id = self.kwargs.get('patient_id')
        patient = models.Patient.objects.get(id=patient_id)
        patient_record, created = self.model.objects.get_or_create(patient=patient)
        return patient_record



class PatientListView(generic.TemplateView):
    template_name = 'search.html'
