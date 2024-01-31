"""
URL configuration for gendarmerie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auteurs import views as auteur
from authentication import views as authentication
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('signup/', authentication.SignupView.as_view(), name='signup'),
    path('logout/', authentication.LogoutView, name='logout'),
    path('auteur/', auteur.auteur_list, name='auteur-list'),
    path('auteur/create_auteur/', auteur.auteur_create, name='auteur-create'),
    path('auteur/<int:id>/', auteur.auteur_retrieve, name='auteur-details'),
    path('auteur/<int:id>/update/', auteur.auteur_update, name='auteur-update'),
    path('auteur/<int:id>/delete/', auteur.auteur_destroy, name='auteur-delete'),
    path('auteur/statistiques/', auteur.auteur_statistique, name='auteur-statistiques'),
]
