from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView

from equation.models import Parameter, Answer
from equation.forms import ParameterForm


class EquationView(FormView):
    template_name = 'equation/equation.html'
    form_class = ParameterForm
    success_url = reverse_lazy('equation:equation_view')

    def get_context_data(self, **kwargs):
        context = super(EquationView, self).get_context_data(**kwargs)
        return context


