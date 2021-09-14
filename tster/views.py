import time

from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.jinja"

    def get_context_data(self, **kwargs):
        kwargs.update({"mytime": time.time()})
        return super().get_context_data(**kwargs)
