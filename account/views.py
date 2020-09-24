from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):

    template_name = 'account/facebook_login.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, *args, **kwargs):
        pass
