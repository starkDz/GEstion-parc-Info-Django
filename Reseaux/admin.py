from django.contrib import admin
from .models import Usage,Type_arm,Type_equipement,Armoire,Equipement
from Equipement.models import Etat

class EquipementAdmin(admin.ModelAdmin):
    list_display= ('Type','n_serie','armoire','etat_equipement')
    list_filter = ('usage','armoire')

# Register your models here.
admin.site.register(Usage)
admin.site.register(Type_arm)
admin.site.register(Type_equipement)
admin.site.register(Armoire)
admin.site.register(Equipement, EquipementAdmin)