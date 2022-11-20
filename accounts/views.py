from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
import mixins

class DashboardView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard.html'



class UserTypeRedirectView(generic.RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        print('user type', user.user_type)
        if user.is_superuser:
            return reverse_lazy('home')
        if user.user_type == user.USER_TYPE_DOCTOR or \
                user.user_type == user.USER_TYPE_LAB_TECHNICIAN:
            return reverse_lazy('patient_list')
        elif user.user_type == user.USER_TYPE_CASHIER:
            return reverse_lazy('home')
        else:
            return reverse_lazy('home')
