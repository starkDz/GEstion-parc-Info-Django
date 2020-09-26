from django.contrib import admin
from .models import Article,Marque_Consommable,Type_Consommable,Model_Consommable

class ArticleAdmin(admin.ModelAdmin):
    list_display= ('Type','Service')
    list_filter = ('Service_FK','Type_Article_FK')
    search_fields = ('Type_Article_FK','Service_FK')

class Type_ConsommableAdmin(admin.ModelAdmin):
    list_display = ('Designation_Type',)
class Marque_ConsommableAdmin(admin.ModelAdmin):
    list_display = ('Designation_Marque',)
class Model_ConsommableAdmin(admin.ModelAdmin):
    list_display = ('Designation_Model',)
# Register your models here.
admin.site.register(Type_Consommable,Type_ConsommableAdmin)
admin.site.register(Marque_Consommable,Marque_ConsommableAdmin)
admin.site.register(Model_Consommable,Model_ConsommableAdmin)
admin.site.register(Article,ArticleAdmin)
