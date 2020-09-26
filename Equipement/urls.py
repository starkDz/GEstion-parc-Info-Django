"""gestion_materiel_informatique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:materiel_id>/',views.detail,name='detail'),
    path('toutes_les_equipements/',views.detail_all,name='detail_all'),
    path('print/',views.imprimer_tout,name='equipement'),
    path('print/<int:equipement_id>/',views.imprimer,name='equipement'),
    path('printPerService/<int:service_id>/',views.imprimerPerService,name='imprimerPerService'),
    path('Stock/',views.detail_Magasin,name='detail_all'),
    path('OutStock/',views.detail_OutMagasin,name='detail_all'),
]
