from django.db import models
from Equipement.models import Etat

# Create your models here.


class Usage(models.Model):
	description=models.CharField(max_length=250,default='')
	def __str__(self):
		return self.description
	class Meta:
		verbose_name_plural = "Usages"


class Type_arm(models.Model):
	description=models.CharField(max_length=250,default='')
	def __str__(self):
		return self.description
	class Meta:
		verbose_name_plural = "Types des armoires"

class Type_equipement(models.Model):
	description=models.CharField(max_length=250,default='')
	def __str__(self):
		return self.description
	class Meta:
		verbose_name_plural = "Types des equipements"

class Armoire(models.Model):
	position=models.CharField(max_length=250,default='')
	type_armoire=models.ForeignKey(Type_arm,on_delete=models.CASCADE)
	def __str__(self):
		return self.position
	class Meta:
		verbose_name_plural = "Armoires"

class Equipement(models.Model):
	reference=models.CharField(max_length=250,default='')
	n_serie=models.CharField(max_length=250,default='')
	ip=models.CharField(max_length=250,default='')
	mac=models.CharField(max_length=250,default='')
	version=models.CharField(max_length=250,default='')
	anne=models.CharField(max_length=250,default='')
	etat_equipement=models.ForeignKey(Etat,on_delete=models.CASCADE)
	type_equipement=models.ForeignKey(Type_equipement,on_delete=models.CASCADE)
	usage=models.ForeignKey(Usage,on_delete=models.CASCADE)
	armoire=models.ForeignKey(Armoire,on_delete=models.CASCADE)
	software=models.CharField(max_length=250,default='')
	def __str__(self):
		return self.reference

	def Type(self):
		return self.type_equipement
	class Meta:
		verbose_name_plural = "Equipements"
