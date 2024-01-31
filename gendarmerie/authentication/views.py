from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.conf import settings

# Create your views here.
from authentication.forms import LoginForm

from authentication.forms import SignupForm


class LoginView(View):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, {"form": form, "message": message})

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('auteur-statistiques')
            else:
                message = 'Identifiants invalides.'

            return render(request, self.template_name, {"form": form, "message": message})


def LogoutView(request):
    logout(request)
    return redirect('login')


class SignupView(View):
    form_class = SignupForm
    template_name = 'signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name, {"form": form})

