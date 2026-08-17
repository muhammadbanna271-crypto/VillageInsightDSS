from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView


class BaseDetailView(LoginRequiredMixin, DetailView):
    """
    Semua user yang login boleh lihat detail.
    """

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["can_edit"] = (
            self.request.user.is_staff
            or self.request.user.is_superuser
        )

        return context