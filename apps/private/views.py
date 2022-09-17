from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.authentication.mixins import GroupRequiredMixin


class Private(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = 'private_home/index.html'
    login_url = 'login'
    group_required = ['nivel_2']

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print('Entra el contexto')
        return self.render_to_response(context)
