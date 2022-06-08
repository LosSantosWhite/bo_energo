from django.urls import path

from equation.views import EquationView

app_name = "equation"


urlpatterns = [
    path('solve/', EquationView.as_view(), name='equation_view'),
]