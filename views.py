from django.views.generic import TemplateView
import mixins


class HomeView(mixins.LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
