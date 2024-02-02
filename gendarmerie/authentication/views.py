from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.conf import settings

from authentication.forms import LoginForm, SignupForm

from pictures.forms import ImageForm

from authentication.models import User


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
        profile_picture = ImageForm()
        return render(request, self.template_name, {"form": form, "profile_picture": profile_picture})

    def post(self, request):
        form = self.form_class(request.POST)
        profile_photo = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            if profile_photo.is_valid():
                user.save()
                image_instance = profile_photo.save(commit=False)
                image_instance.uploader = user
                image_instance.save()
                user.profile_photo = image_instance
            user.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name, {"form": form})


def list_user(request):
    users = User.objects.all()

    return render(request, 'user_list.html', {"users": users})