from django import forms
from Equipement.models import Service

def get_choices():
    Services=Service.objects.all()
    CHOICE=[]
    i=0
    while True:
        CHOICE.append((Services[i].Designation_Service,Services[i].Designation_Service))
        if i>=Services.count()-1:
            break
        i=i+1
    return CHOICE

class NameForm(forms.Form):
    num_c12=forms.CharField(label="numero C12",max_length=100)
    date_C12=forms.DateField(label="date C12")
    quantite=forms.IntegerField(label="quantite")
    service=forms.CharField(widget=forms.Select(choices=get_choices()))
