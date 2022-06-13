from django.urls import path

from assignment.views import GetItemView

app_name = "assignment"

urlpatterns = [
    path("get-item/", GetItemView.as_view(), name="get_item_view"),
]
