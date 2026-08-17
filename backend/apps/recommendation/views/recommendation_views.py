"""
Replace isi apps/recommendation/views/recommendation_views.py
dengan ini. Tambahin juga path baru di urls.py (contoh di bawah).
"""

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from apps.recommendation.services import RecommendationService


def recommendation_dashboard(request):
    """
    Semua orang (termasuk visitor / belum login) boleh lihat --
    tapi cuma baca dari cache, TIDAK menghitung ulang.
    """

    context = RecommendationService.dashboard()

    # is_superuser dikirim ke template, dipakai buat nampilin
    # tombol "Hitung Ulang" cuma buat superuser.
    context["can_recalculate"] = (
        request.user.is_authenticated and request.user.is_superuser
    )

    return render(
        request,
        "recommendation/dashboard.html",
        context,
    )


@login_required
@user_passes_test(lambda u: u.is_superuser)
def recalculate_recommendation(request):
    """
    Cuma superuser yang bisa trigger hitung ulang. Kalau visitor
    atau user biasa coba akses URL ini langsung, otomatis di-
    redirect ke halaman login (login_required) atau ditolak
    (user_passes_test) sebelum masuk ke sini sama sekali.
    """

    if request.method == "POST":

        RecommendationService.recalculate()

        messages.success(
            request,
            "Hasil rekomendasi berhasil dihitung ulang.",
        )

    return redirect("recommendation:dashboard")


# --------------------------------------------------------------
# Tambahan di apps/recommendation/urls/recommendation_urls.py:
#
# from apps.recommendation.views.recommendation_views import (
#     recommendation_dashboard,
#     recalculate_recommendation,
# )
#
# urlpatterns = [
#     path("", recommendation_dashboard, name="dashboard"),
#     path(
#         "recalculate/",
#         recalculate_recommendation,
#         name="recalculate",
#     ),
#     ...
# ]
# --------------------------------------------------------------