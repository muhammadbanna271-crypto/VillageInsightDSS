from django.contrib import messages
from django.views.generic import DeleteView


class BaseDeleteView(DeleteView):
    """
    Base Delete View
    """

    success_message = "Data deleted successfully."

    def form_valid(self, form):

        messages.success(
            self.request,
            self.success_message,
        )

        return super().form_valid(form)