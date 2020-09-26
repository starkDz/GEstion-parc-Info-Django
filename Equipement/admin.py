from django.contrib import admin
from .models import Kit,Materiel,Type_Materiel,Marque,Model_Materiel,Service,Etat


class ServiceAdmin(admin.ModelAdmin):
    list_display= ('id','Nom_Service','Designation_Service','Service_Pere')
    list_filter = ('Service_Per','Designation_Service')
    search_fields = ('Service_Per','Designation_Service')

class MaterielAdmin(admin.ModelAdmin):
    list_display= ('Type','Num_Serie','Address_Mac','Service','Etat')
    list_filter = ('Service_FK','Type_Materiel_FK')
    search_fields = ('Type_Materiel_FK','Service_FK')

class Model_MaterielAdmin(admin.ModelAdmin):
    list_display= ('id','Designation_Model')

class MarqueAdmin(admin.ModelAdmin):
    list_display= ('id','Designation_Marque')

class Type_MaterielAdmin(admin.ModelAdmin):
    list_display= ('id','Designation_Type')

class KitAdmin(admin.ModelAdmin):
    list_display= ('id','Designation_Kit')

class EtatAdmin(admin.ModelAdmin):
    list_display= ('id','Designation_Etat')

# Register your models here.
admin.site.register(Materiel, MaterielAdmin)
admin.site.register(Type_Materiel,Type_MaterielAdmin)
admin.site.register(Marque,MarqueAdmin)
admin.site.register(Model_Materiel,Model_MaterielAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Etat,EtatAdmin)
admin.site.register(Kit,KitAdmin)
