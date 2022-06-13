from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from equation.forms import ParameterForm
from equation.controllers import get_roots


class EquationView(FormView):
    template_name = "equation/equation.html"
    form_class = ParameterForm
    success_url = reverse_lazy("equation:equation_view")

    def post(self, request, *args, **kwargs):
        form = ParameterForm(data=self.request.POST)
        result = [
            self.request.POST["a"],
            self.request.POST["b"],
            self.request.POST["c"],
        ]
        result = list(map(float, result))
        result = get_roots(a=result[0], b=result[1], c=result[2])
        context = {
            "form": form,
        }

        if len(result) == 0:
            context["result"] = "No real roots"
        else:
            context["result"] = result

        return render(request, self.template_name, context)
