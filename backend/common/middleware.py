from django.conf import settings
from django.shortcuts import redirect
from django.urls import resolve, reverse


class LoginRequiredMiddleware:
    """
    Memaksa semua halaman login terlebih dahulu,
    kecuali halaman yang memang diizinkan.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:
            return self.get_response(request)

        current_url = resolve(request.path_info).url_name

        allowed_urls = {
            "login",
            "logout",
        }

        if current_url in allowed_urls:
            return self.get_response(request)

        if request.path.startswith(settings.STATIC_URL):
            return self.get_response(request)

        if request.path.startswith("/admin/login"):
            return self.get_response(request)

        return redirect(
            f"{reverse('login')}?next={request.path}"
        )