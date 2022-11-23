from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
import mixins
from records.models import PatientRecord


class UserTypeRedirectView(mixins.LoginRequiredMixin, generic.RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('dashboard')


class DashboardView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        user = self.request.user
        if user.is_staff or user.is_doctor:
            context['patients_pending_consultation'] = PatientRecord.objects.filter(
                Q(signs_and_symptoms__exact='') &
                Q(test__exact='')
            )
        if user.is_staff or user.is_lab_technician:
            context['patients_pending_lab_tests'] = PatientRecord.objects.filter(
                ~Q(signs_and_symptoms__exact='') &
                ~Q(test__exact='') &
                Q(test_result__exact='')
            )
        if user.is_staff or user.is_doctor:
            context['patients_pending_treatment'] = PatientRecord.objects.filter(
                ~Q(signs_and_symptoms__exact='') &
                ~Q(test__exact='') &
                ~Q(test_result__exact='') &
                Q(treatment__exact='')
            )
        if user.is_staff:
            context['discharged_patients'] = PatientRecord.objects.filter(
                ~Q(signs_and_symptoms__exact='') &
                ~Q(test__exact='') &
                ~Q(test_result__exact='') &
                ~Q(treatment__exact='')
            )
        if user.is_superuser or user.is_staff:
            context['title'] = "Admin's Dashboard"
            context['patients'] = PatientRecord.objects.all()
        elif user.is_doctor:
            context['title'] = "Doctor's Dashboard"
        elif user.is_cashier:
            context['title'] = 'Registry Dashboard'
        elif user.is_lab_technician:
            context['title'] = "Lab Technician's Dashboard"
        elif user.is_pharmacist:
            context['title'] = "Pharmacist's Dashboard"
        return context
