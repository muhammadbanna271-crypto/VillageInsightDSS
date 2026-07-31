from django.urls import reverse_lazy

from common.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseUpdateView,
)

from apps.master.forms import VariableForm
from apps.master.models import Variable


class VariableListView(BaseListView):
    model = Variable
    template_name = "master/variable/list.html"
    context_object_name = "variables"
    ordering = ["code"]
    search_fields = [
        "code",
        "name",
    ]


class VariableDetailView(BaseDetailView):
    model = Variable
    template_name = "master/variable/detail.html"
    context_object_name = "variable"


class VariableCreateView(BaseCreateView):
    model = Variable
    form_class = VariableForm
    template_name = "master/variable/create.html"
    success_url = reverse_lazy("master:variable-list")
    success_message = "Variable created successfully."


class VariableUpdateView(BaseUpdateView):
    model = Variable
    form_class = VariableForm
    template_name = "master/variable/update.html"
    success_url = reverse_lazy("master:variable-list")
    success_message = "Variable updated successfully."


class VariableDeleteView(BaseDeleteView):
    model = Variable
    template_name = "master/variable/delete.html"
    success_url = reverse_lazy("master:variable-list")
    success_message = "Variable deleted successfully."