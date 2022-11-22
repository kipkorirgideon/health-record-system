from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic

from django_tables2 import SingleTableView, LazyPaginator

from . import forms, tables
from . import models
import mixins


# Create your views here.
class PatientRecordTableListView(SingleTableView):
    model = models.PatientRecord
    table_class = tables.PatientTable
    template_name = 'patient_list.html'
    context_object_name = 'patients'

    table_pagination = {
        'per_page': 10
    }
    paginator_class = LazyPaginator


class PatientRegisterView(mixins.LoginRequiredMixin, PatientRecordTableListView):
    pass


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
        return self.model.objects.get(uuid=patient_uuid)


class PatientDoctorUpdateView(mixins.LoginRequiredMixin, PatientRecordUpdateView):
    form_class = forms.PatientDoctorUpdateForm
    success_url = reverse_lazy('dashboard')


class PatientLabTestUpdateView(mixins.LoginRequiredMixin, PatientRecordUpdateView):
    form_class = forms.PatientLabTestUpdateForm
    success_url = reverse_lazy('dashboard')


class PatientListView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = self.request.user.user_type
        return context


class PendingConsultationListView(mixins.LoginRequiredMixin, PatientRecordTableListView):
    table_class = tables.PatientRecordPendingConsultationTable

    def get_queryset(self):
        return self.model.objects.filter(
            Q(signs_and_symptoms__exact='') &
            Q(test__exact=''))


class PendingLabTestListView(mixins.LoginRequiredMixin, PatientRecordTableListView):
    table_class = tables.PatientRecordPendingLabTestTable

    def get_queryset(self):
        return self.model.objects.filter(test_result__exact='')


class PendingTreatmentListView(mixins.LoginRequiredMixin, PatientRecordTableListView):
    table_class = tables.PatientRecordPendingTreatmentTable

    def get_queryset(self):
        return self.model.objects.filter(treatment__exact='')


class PatientDetailView(mixins.LoginRequiredMixin, generic.DetailView):
    model = models.PatientRecord
    template_name = 'patient_detail.html'
    context_object_name = 'patient'
    pk_url_kwarg = 'patient_uuid'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = self.request.user.user_type
        return context

    def get_object(self, queryset=None):
        patient_uuid = self.kwargs.get('patient_uuid')
        return self.model.objects.get(uuid=patient_uuid)


class PatientTreatmentUpdateView(mixins.LoginRequiredMixin, PatientRecordUpdateView):
    form_class = forms.PatientTreatmentUpdateForm
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        return reverse_lazy('patient_detail', kwargs={'patient_uuid': self.object.uuid})
