from django.contrib import messages
from django.views.generic import UpdateView


class BaseUpdateView(UpdateView):
    """
    Base Update View
    """

    success_message = "Data updated successfully."

    def form_valid(self, form):

        messages.success(
            self.request,
            self.success_message,
        )

        return super().form_valid(form)