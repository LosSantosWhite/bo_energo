from django.contrib import admin
from equation.models import Answer, Parameter


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ["a", "b", "c"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["x_1", "x_2"]
