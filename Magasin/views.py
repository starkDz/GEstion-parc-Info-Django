from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse
from Equipement.models import Type_Materiel,Service
from Reseaux.models import Type_equipement
from .models import Article,Type_Consommable
from django.db.models import Q

# Create your views here.
def index(request):
    type_de_materiel=Type_Materiel.objects.all()
    type_de_materiel_reseaux=type_equipement.objects.all()
    Article_consommable=Article.objects.all()
    return TemplateResponse(request,'details_consommable.html',{'Article_consommable':Article_consommable,'type_de_materiel':type_de_materiel,'type_de_materiel_reseaux':type_de_materiel_reseaux})

def detail(request,article_id):
    type_id=str(article_id)
    liste_materiel=Article.objects.all().filter(Type_Article_FK=type_id)
    type_de_materiel=Type_Materiel.objects.all()
    type_de_consommable=Type_Consommable.objects.all()
    Services=Service.objects.all()
    type_de_materiel_reseaux=Type_equipement.objects.all()
    return TemplateResponse(request,'details_consommable.html',{'type_de_materiel':type_de_materiel,'Services':Services,'type_de_materiel_reseaux':type_de_materiel_reseaux,"liste_materiel":liste_materiel,'type_de_consommable':type_de_consommable})

def detail_all(request):
    liste_materiel=Article.objects.all()
    type_de_materiel=Type_Materiel.objects.all()
    type_de_consommable=Type_Consommable.objects.all()
    Services=Service.objects.all()
    type_de_materiel_reseaux=Type_equipement.objects.all()
    return TemplateResponse(request,'details_consommable.html',{"liste_materiel":liste_materiel,'Services':Services,'type_de_materiel_reseaux':type_de_materiel_reseaux,'type_de_materiel':type_de_materiel,'type_de_consommable':type_de_consommable})

def detail_Magasin(request):
    liste_materiel=Article.objects.all().filter(Service_FK='60')
    type_de_materiel=Type_Materiel.objects.all()
    type_de_consommable=Type_Consommable.objects.all()
    Services=Service.objects.all()
    type_de_materiel_reseaux=Type_equipement.objects.all()
    return TemplateResponse(request,'details_consommable.html',{"liste_materiel":liste_materiel,'Services':Services,'type_de_materiel_reseaux':type_de_materiel_reseaux,'type_de_materiel':type_de_materiel,'type_de_consommable':type_de_consommable})

def detail_OutMagasin(request):
    liste_materiel=Article.objects.all().filter(~Q(Service_FK='60'))
    type_de_materiel=Type_Materiel.objects.all()
    type_de_consommable=Type_Consommable.objects.all()
    Services=Service.objects.all()
    type_de_materiel_reseaux=Type_equipement.objects.all()
    return TemplateResponse(request,'details_consommable.html',{"liste_materiel":liste_materiel,'Services':Services,'type_de_materiel_reseaux':type_de_materiel_reseaux,'type_de_materiel':type_de_materiel,'type_de_consommable':type_de_consommable})
