from django.views.generic import ListView
from django.db.models import Q


class BaseListView(ListView):

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