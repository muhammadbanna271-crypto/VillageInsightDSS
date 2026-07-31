from django.shortcuts import render

from apps.recommendation.services import (
    RecommendationService,
)


def recommendation_dashboard(request):

    context = RecommendationService.dashboard()

    return render(
        request,
        "recommendation/dashboard.html",
        context,
    )