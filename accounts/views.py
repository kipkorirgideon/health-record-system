from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
import mixins
from records.models import Patient


class DashboardView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        user = self.request.user
        context['patients_pending_lab_tests'] = Patient.objects.filter(
            Q(record__signs_and_symptoms__exact='') &
            Q(record__test_result__exact=''))

        context['patients_pending_treatment'] = Patient.objects.filter(
            Q(record__signs_and_symptoms__exact='') &
            Q(record__treatment__exact=''))
        return context


class UserTypeRedirectView(generic.RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return reverse_lazy('home')
        if user.user_type == user.USER_TYPE_DOCTOR or \
                user.user_type == user.USER_TYPE_LAB_TECHNICIAN:
            return reverse_lazy('patient_list')
        elif user.user_type == user.USER_TYPE_CASHIER:
            return reverse_lazy('home')
        else:
            return reverse_lazy('home')
