from django.db import models
from Equipement.models import Type_Materiel,Model_Materiel,Marque,Service


class Model_Consommable(models.Model):
	Designation_Model=models.CharField(max_length=250)
	Annee=models.DateField(null=True, blank=True)
	def __str__(self):
		return self.Designation_Model
	class Meta:
		verbose_name_plural = "Models des Consommable"


class Marque_Consommable(models.Model):
	Designation_Marque=models.CharField(max_length=250)
	Pays=models.CharField(max_length=20,null=True, blank=True)
	def __str__(self):
		return self.Designation_Marque
	class Meta:
		verbose_name_plural = "Marques des Consommable"

class Type_Consommable(models.Model):
	Designation_Type=models.CharField(max_length=250)
	def __str__(self):
		return self.Designation_Type
	class Meta:
		verbose_name_plural = "Types des Consommable"


class Article(models.Model):
	Type_Article_FK=models.ForeignKey(Type_Consommable,on_delete=models.CASCADE)
	Model_Article_FK=models.ForeignKey(Model_Consommable,blank=True, null=True, on_delete=models.CASCADE)
	Marque_FK=models.ForeignKey(Marque_Consommable,on_delete=models.CASCADE)
	Description=models.CharField(max_length=250,default='/')
	Service_FK=models.ForeignKey(Service,on_delete=models.CASCADE,default='60')
	Num_OrdM=models.CharField(max_length=30,blank=True, null=True)
	Date_OrdM=models.DateField(null=True, blank=True)
	Num_C12=models.CharField(max_length=30,blank=True, null=True)
	Date_C12=models.DateField(null=True, blank=True)
	Quantite=models.PositiveIntegerField(default=1)

	def Type(self):
	    return self.Type_Article_FK
	def Service(self):
	    return self.Service_FK
	class Meta:
	    verbose_name_plural = "Articles"
