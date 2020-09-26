from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.template.response import TemplateResponse
import os
from reportlab.pdfgen import canvas
import subprocess
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter, landscape
from .models import Materiel,Type_Materiel,Service
from Reseaux.models import Usage,Type_arm,Type_equipement,Armoire,Equipement
from Magasin.models import Type_Consommable,Article,Marque_Consommable
from django.db.models import Q

from django.shortcuts import render
from .forms import NameForm

def index(request):
    type_de_materiel=Type_Materiel.objects.all()
    type_de_materiel_reseaux=Type_equipement.objects.all()
    Services=Service.objects.all()
    type_de_consommable=Type_Consommable.objects.all()
    return TemplateResponse(request,'base.html',{'type_de_materiel':type_de_materiel,'type_de_consommable':type_de_consommable,'Services':Services,'type_de_materiel_reseaux':type_de_materiel_reseaux})

def documents(request,materiel_id):
    type_de_materiel=Type_Materiel.objects.all()
    type_de_materiel_reseaux=Type_equipement.objects.all()
    Services=Service.objects.all()
    form = NameForm()
    type_de_consommable=Type_Consommable.objects.all()
    materiel_id=str(materiel_id)
    mat=Article.objects.get(id=materiel_id)
    return TemplateResponse(request,'distribution.html',{'mat':mat,'form':form,'type_de_materiel':type_de_materiel,'type_de_consommable':type_de_consommable,'Services':Services,'type_de_materiel_reseaux':type_de_materiel_reseaux})



def distributionForm(request,id):
    id_art=str(id)
    articleDistr=Article.objects.get(id=id_art)
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            num=request.POST.get('num_c12')
            date=request.POST.get('date_C12')
            quantite=request.POST.get('quantite')
            service=request.POST.get('service')
            newVal=articleDistr.Quantite-int(quantite)
            articleDistr.Quantite=newVal
            articleDistr.save()
            p=Article.objects.create(Num_C12=num,Date_C12=date,Service_FK=Service.objects.get(Designation_Service=service),Marque_FK=Marque_Consommable.objects.get(Designation_Marque=articleDistr.Marque_FK),Type_Article_FK=Type_Consommable.objects.get(Designation_Type=articleDistr.Type_Article_FK),Quantite=quantite)
            liste_materiel=Article.objects.all().filter(Service_FK='60')
            type_de_materiel=Type_Materiel.objects.all()
            type_de_consommable=Type_Consommable.objects.all()
            Services=Service.objects.all()
            type_de_materiel_reseaux=Type_equipement.objects.all()
            return TemplateResponse(request,'details_consommable.html',{"liste_materiel":liste_materiel,'Services':Services,'type_de_materiel_reseaux':type_de_materiel_reseaux,'type_de_materiel':type_de_materiel,'type_de_consommable':type_de_consommable})

    else:
        form = NameForm()
    return render(request,'distribution.html',{'form':form})

def detail(request,materiel_id):
    type_id=str(materiel_id)
    liste_materiel=Materiel.objects.all().filter(Type_Materiel_FK=type_id)
    type_de_materiel=Type_Materiel.objects.all()
    type_de_consommable=Type_Consommable.objects.all()
    Services=Service.objects.all()
    type_de_materiel_reseaux=Type_equipement.objects.all()
    return TemplateResponse(request,'details.html',{"liste_materiel":liste_materiel,'type_de_consommable':type_de_consommable,'Services':Services,'type_de_materiel_reseaux':type_de_materiel_reseaux,'type_de_materiel':type_de_materiel})

def detail_all(request):
    liste_materiel=Materiel.objects.all()
    type_de_materiel=Type_Materiel.objects.all()
    Services=Service.objects.all()
    type_de_consommable=Type_Consommable.objects.all()
    type_de_materiel_reseaux=Type_equipement.objects.all()
    return TemplateResponse(request,'details.html',{"liste_materiel":liste_materiel,'type_de_consommable':type_de_consommable,'Services':Services,'type_de_materiel_reseaux':type_de_materiel_reseaux,'type_de_materiel':type_de_materiel})

def imprimer_tout(request):
    liste_materiel=Materiel.objects.all().order_by('Kit_FK')
    type_de_materiel=Type_Materiel.objects.all()
    Services=Service.objects.all()
    type_de_consommable=Type_Consommable.objects.all()
    type_de_materiel_reseaux=Type_equipement.objects.all()
    c=canvas.Canvas("pdf_set.pdf", pagesize=landscape(letter))
    pos=415
    kit='a'
    i=0
    while True:
        c.drawString(280,pos,"1")
        c.drawString(320,pos,"1")
        c.drawString(350,pos,str(liste_materiel[i].Type_Materiel_FK))
        c.drawString(500,pos,str(liste_materiel[i].Num_Serie))
        pos=pos-20
        if i>=liste_materiel.count()-1:
            break

        if (liste_materiel[i].Kit_FK != liste_materiel[i+1].Kit_FK) :
            c.drawString(700,550,str(liste_materiel[i].Service_FK))
            c.showPage()
            pos=415
        i=i+1
    c.drawString(700,550,str(liste_materiel[i].Service_FK))
    c.showPage()

    c.save()
    subprocess.Popen(['pdf_set.pdf'], shell=True)
    return TemplateResponse(request,'base.html',{'type_de_materiel':type_de_materiel,'type_de_consommable':type_de_consommable,'Services':Services,'type_de_materiel_reseaux':type_de_materiel_reseaux})


def imprimer(request,equipement_id):
    type_de_materiel=Type_Materiel.objects.all()
    type_de_consommable=Type_Consommable.objects.all()
    type_id=str(equipement_id)
    liste_materiel=Materiel.objects.get(id=type_id)                 # imprimer specifique Type d'Equipements
    #liste_materiel=Materiel.objects.all().filter(id=type_id)                              imprimer Equipement spectifique
    c=canvas.Canvas("pdf_set.pdf", pagesize=landscape(letter))
    Services=Service.objects.all()
    c.drawString(280,415,"1")
    c.drawString(320,415,"1")
    c.drawString(350,415,str(liste_materiel[0].Type_Materiel_FK))
    c.drawString(500,415,str(liste_materiel[0].Num_Serie))
    Ser=str(liste_materiel[0].Service_FK)
    String=Ser
    while True:
        serv=Service.objects.filter(Designation_Service=Ser)
        Ser=serv[0].Service_Per
        String=String+" / "+str(Ser)
        if(str(Ser) == "ESTA"):
            break

    c.drawString(500,550,str(String))

    c.showPage()

    c.save()
    subprocess.Popen(['pdf_set.pdf'], shell=True)
    return TemplateResponse(request,'base.html',{'type_de_materiel':type_de_materiel,'type_de_consommable':type_de_consommable,'Services':Services})


def imprimerPerService(request,service_id):
    type_de_materiel=Type_Materiel.objects.all()
    ser_id=str(service_id)
    type_de_consommable=Type_Consommable.objects.all()
    Services=Service.objects.all()
    liste_materiel=Materiel.objects.all().filter(Service_FK=ser_id)                 # Imprimer specifique Type d'Equipements
    #liste_materiel=Materiel.objects.all().filter(id=type_id)                              imprimer Equipement spectifique
    c=canvas.Canvas("pdf_set.pdf", pagesize=landscape(letter))
    i=1
    pos=415
    if(liste_materiel.count()>0):
        while True:
            c.drawString(700,550,str(liste_materiel[i-1].Service_FK))
            c.drawString(280,pos,"1")
            c.drawString(320,pos,"1")
            c.drawString(350,pos,str(liste_materiel[i-1].Type_Materiel_FK))
            c.drawString(500,pos,str(liste_materiel[i-1].Num_Serie))
            pos=pos-20
            if i%12==0:
                pos=415
                c.drawString(700,550,str(liste_materiel[i-1].Service_FK))
                c.showPage()

            if i>=liste_materiel.count():
                break
            i=i+1

        c.save()
        subprocess.Popen(['pdf_set.pdf'], shell=True)
    return TemplateResponse(request,'base.html',{'type_de_materiel':type_de_materiel,'type_de_consommable':type_de_consommable,'Services':Services})

def detail_Magasin(request):
    liste_materiel=Materiel.objects.all().filter(Service_FK='60')
    type_de_materiel=Type_Materiel.objects.all()
    type_de_consommable=Type_Consommable.objects.all()
    Services=Service.objects.all()
    type_de_materiel_reseaux=Type_equipement.objects.all()
    return TemplateResponse(request,'details.html',{"liste_materiel":liste_materiel,'Services':Services,'type_de_materiel_reseaux':type_de_materiel_reseaux,'type_de_materiel':type_de_materiel,'type_de_consommable':type_de_consommable})

def detail_OutMagasin(request):
    liste_materiel=Materiel.objects.all().filter(~Q(Service_FK='60'))
    type_de_materiel=Type_Materiel.objects.all()
    type_de_consommable=Type_Consommable.objects.all()
    Services=Service.objects.all()
    type_de_materiel_reseaux=Type_equipement.objects.all()
    return TemplateResponse(request,'details.html',{"liste_materiel":liste_materiel,'Services':Services,'type_de_materiel_reseaux':type_de_materiel_reseaux,'type_de_materiel':type_de_materiel,'type_de_consommable':type_de_consommable})
