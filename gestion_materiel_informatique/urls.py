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
from django.contrib import admin
from django.urls import include,path
from Equipement import views

admin.site.site_header = "Administration Gestion Materiels Informatique"
admin.site.site_title = "GMI admin"
admin.site.index_title = "Bienvenue"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('Documents/<int:materiel_id>/', views.documents,name='index'),
    path('equipement/', include('Equipement.urls')),
    path('Reseaux/', include('Reseaux.urls')),
    path('Magasin/', include('Magasin.urls')),
    path('distributionForm/<int:id>/',views.distributionForm,name='testForm'),
]
