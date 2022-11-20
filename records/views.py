from django.urls import reverse_lazy
from django.views import generic

from django_tables2 import SingleTableView, LazyPaginator

from . import forms, tables
from . import models
import mixins


# Create your views here.

class PatientRegisterView(mixins.LoginRequiredMixin, SingleTableView):
    model = models.Patient
    table_class = tables.PatientTable
    template_name = 'cashier_patient_create.html'

    table_pagination = {
        'per_page': 10
    }
    paginator_class = LazyPaginator


class PatientCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Patient
    form_class = forms.PatientCreateForm
    template_name = 'patient_create.html'
    success_url = reverse_lazy('patient_register')


class PatientRecordUpdateView(generic.UpdateView):
    model = models.PatientRecord
    form_class = None
    template_name = 'patient_records_update.html'
    success_url = None
    pk_url_kwarg = 'patient_uuid'

    def get_object(self, queryset=None):
        patient_uuid = self.kwargs.get('patient_uuid')
        patient = models.Patient.objects.get(uuid=patient_uuid)
        patient_record, created = self.model.objects.get_or_create(patient=patient)
        return patient_record


class PatientDoctorUpdateView(mixins.LoginRequiredMixin, PatientRecordUpdateView):
    form_class = forms.PatientDoctorUpdateForm
    success_url = reverse_lazy('patient_list')


class PatientLabTestUpdateView(mixins.LoginRequiredMixin, PatientRecordUpdateView):
    form_class = forms.PatientLabTestUpdateForm
    success_url = reverse_lazy('patient_list')


class PatientListView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = self.request.user.user_type
        return context
