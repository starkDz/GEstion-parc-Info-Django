from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse
from .models import Usage,Type_arm,Type_equipement,Armoire,Equipement
from Equipement.models import Materiel,Type_Materiel
from Magasin.models import Type_Consommable
# Create your views here.
def index(request):
    type_de_consommable=Type_Consommable.objects.all()
    type_de_materiel=Type_Materiel.objects.all()
    type_de_materiel_reseaux=type_equipement.objects.all()
    return TemplateResponse(request,'base.html',{'type_de_materiel':type_de_materiel,'type_de_consommable':type_de_consommable,'type_de_materiel_reseaux':type_de_materiel_reseaux})


def detail(request,materiel_id):
    type_id=str(materiel_id)
    type_de_consommable=Type_Consommable.objects.all()
    liste_materiel=Equipement.objects.all().filter(type_equipement=type_id)
    type_de_materiel_reseaux=Type_equipement.objects.all()
    type_de_materiel=Type_Materiel.objects.all()
    return TemplateResponse(request,'details_reseaux.html',{'type_de_materiel':type_de_materiel,'type_de_consommable':type_de_consommable,"liste_materiel":liste_materiel,'type_de_materiel_reseaux':type_de_materiel_reseaux})

def detail_all(request):
    liste_materiel=Equipement.objects.all()
    type_de_consommable=Type_Consommable.objects.all()
    type_de_materiel_reseaux=Type_equipement.objects.all()
    type_de_materiel=Type_Materiel.objects.all()
    return TemplateResponse(request,'details_reseaux.html',{"liste_materiel":liste_materiel,'type_de_consommable':type_de_consommable,'type_de_materiel':type_de_materiel,'type_de_materiel_reseaux':type_de_materiel_reseaux})
