from django.shortcuts import render, redirect
from django.views.generic import View

from pictures.forms import ImageForm


class ImageView(View):
    form_class = ImageForm
    template_name = 'image.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            image = form.save(commit=False)
            image.uploader = user
            image.save()

            user.profile_photo = image
            user.save()

            return redirect('auteur-statistiques')

        return render(request, self.template_name, {"form": form})

