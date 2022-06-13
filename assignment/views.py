from django.shortcuts import render
from django.views.generic import FormView
from assignment.models import Item
from assignment.forms import ItemForm
from assignment.controllers import fill_db_with_items, refill_db, get_item


class GetItemView(FormView):
    form_class = ItemForm
    template_name = "assignment/index.html"

    def get(self, request, *args, **kwargs):
        if len(Item.objects.all()) == 0:
            fill_db_with_items()
        return super(GetItemView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = ItemForm(data=self.request.POST)

        context = {"color_name": None, "form": form}

        if self.request.POST.get("submit") == "refill":
            refill_db()
        elif self.request.POST.get("number"):
            if int(self.request.POST["number"]) > 100:
                context["color_name"] = "Invalid number, must be lower than 100"
            else:
                context["color_name"] = get_item(int(self.request.POST["number"]))

        return render(request, self.template_name, context)
