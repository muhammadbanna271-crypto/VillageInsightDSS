from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from apps.survey.models import SurveyVillage
from apps.survey.forms import SurveyVillageForm


class SurveyVillageListView(ListView):

    model = SurveyVillage

    template_name = "survey_village/list.html"

    context_object_name = "object_list"

    queryset = (
        SurveyVillage.objects
        .select_related(
            "survey",
            "village",
        )
        .order_by(
            "survey__name",
            "village__name",
        )
    )


class SurveyVillageCreateView(CreateView):

    model = SurveyVillage

    form_class = SurveyVillageForm

    template_name = "survey_village/create.html"

    success_url = reverse_lazy(
        "survey:survey-village-list"
    )


class SurveyVillageUpdateView(UpdateView):

    model = SurveyVillage

    form_class = SurveyVillageForm

    template_name = "survey_village/update.html"

    success_url = reverse_lazy(
        "survey:survey-village-list"
    )


class SurveyVillageDeleteView(DeleteView):

    model = SurveyVillage

    template_name = "survey_village/delete.html"

    success_url = reverse_lazy(
        "survey:survey-village-list"
    )