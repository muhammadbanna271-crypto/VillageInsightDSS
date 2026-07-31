from django.contrib import messages
from django.views.generic import CreateView


class BaseCreateView(CreateView):
    """
    Base Create View
    """

    success_message = "Data created successfully."

    def form_valid(self, form):

        messages.success(
            self.request,
            self.success_message,
        )

        return super().form_valid(form)