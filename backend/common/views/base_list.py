from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.db.models import Q


class BaseListView(LoginRequiredMixin, ListView):
    """
    Semua user yang login (visitor/staff/superuser) boleh lihat.
    """

    paginate_by = 10

    search_fields = []

    def get_queryset(self):

        queryset = super().get_queryset()

        keyword = self.request.GET.get("q")

        if keyword and self.search_fields:

            query = Q()

            for field in self.search_fields:

                query |= Q(**{
                    f"{field}__icontains": keyword
                })

            queryset = queryset.filter(query)

        return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # Dikirim ke SEMUA template list -- dipakai buat
        # nampilin/nyembunyiin tombol Add/Edit/Delete.
        context["can_edit"] = (
            self.request.user.is_staff
            or self.request.user.is_superuser
        )

        return context