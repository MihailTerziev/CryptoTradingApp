from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model, login
from django.views import generic as views
from django.urls import reverse_lazy
from CryptoTradingApp.accounts.forms import UserCreateForm


UserModel = get_user_model()


def index_page(request):
    return render(request, "common/index-home-page.html")


class SignInView(auth_views.LoginView):
    template_name = "users/login-page.html"


class SignUpView(views.CreateView):
    template_name = "users/register-page.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("index-page")

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)
        return response


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy("index-page")
