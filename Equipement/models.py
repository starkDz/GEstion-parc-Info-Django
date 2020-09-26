from django.db import models

# Create your models here.
class Kit(models.Model):
	Designation_Kit=models.CharField(max_length=10,default='0')
	def __str__(self):
		return self.Designation_Kit
	class Meta:
		verbose_name_plural = "Liste des Kits"

class Service(models.Model):
	Nom_Service=models.CharField(max_length=250,default='')
	Designation_Service=models.CharField(max_length=10)
	Service_Per=models.ForeignKey('self',on_delete=models.CASCADE,default=0)
	def __str__(self):
		return self.Designation_Service

	def get_Service_Name(self):
		return self.Nom_Service

	def get_Service_Designation(self):
		return self.Designation_Service

	def Service_Pere(self):
		return self.Service_Per
	class Meta:
		verbose_name_plural = "Services"


class Etat(models.Model):
	Designation_Etat=models.CharField(max_length=250,default='')
	def __str__(self):
		return self.Designation_Etat
	class Meta:
		verbose_name_plural = "Etat des Equipements"



class Model_Materiel(models.Model):
	Designation_Model=models.CharField(max_length=250)
	Annee=models.DateField(null=True, blank=True)
	def __str__(self):
		return self.Designation_Model
	class Meta:
		verbose_name_plural = "Models des Equipements"


class Marque(models.Model):
	Designation_Marque=models.CharField(max_length=250)
	Pays=models.CharField(max_length=20,null=True, blank=True)
	def __str__(self):
		return self.Designation_Marque
	class Meta:
		verbose_name_plural = "Marques"


class Type_Materiel(models.Model):
	Designation_Type=models.CharField(max_length=250)
	def __str__(self):
		return self.Designation_Type
	class Meta:
		verbose_name_plural = "Types des Equipements"


class Type_Document(models.Model):
	Designation_Type_Doc=models.CharField(max_length=250,unique=True)
	def __str__(self):
		template = ' {0.Designation_Type_Doc}'
		return template.format(self)
	class Meta:
		verbose_name_plural = "Types des Documents"



class Document(models.Model):
	Num_Doc=models.CharField(max_length=250,default='')
	Type_Doc_FK=models.ForeignKey(Type_Document,on_delete=models.CASCADE)
	def __str__(self):
		template = 'Num Doc : {0.Num_Doc} {0.Type_Doc_FK}'
		return template.format(self)
	class Meta:
		verbose_name_plural = "Documents"


class Materiel(models.Model):
	Num_Serie=models.CharField(max_length=250,unique=True)
	Model_Materiel_FK=models.ForeignKey(Model_Materiel,blank=True, null=True, on_delete=models.CASCADE)
	Etat_FK=models.ForeignKey(Etat,on_delete=models.CASCADE)
	Marque_FK=models.ForeignKey(Marque,on_delete=models.CASCADE)
	Caracteristiques=models.CharField(max_length=250,default='/')
	Description=models.CharField(max_length=250,default='/')
	Type_Materiel_FK=models.ForeignKey(Type_Materiel,on_delete=models.CASCADE)
	Service_FK=models.ForeignKey(Service,on_delete=models.CASCADE)
	Kit_FK=models.ForeignKey(Kit,blank=True, null=True,on_delete=models.CASCADE)
	Address_Mac=models.CharField(max_length=30,blank=True, null=True)
	Num_OrdM=models.CharField(max_length=30,blank=True, null=True)
	Date_OrdM=models.DateField(null=True, blank=True)
	Num_C12=models.CharField(max_length=30,blank=True, null=True)
	Date_C12=models.DateField(null=True, blank=True)
	Num_C7=models.CharField(max_length=30,blank=True, null=True)
	Date_C7=models.DateField(null=True, blank=True)
	Num_C5=models.CharField(max_length=30,blank=True, null=True)
	Date_C5=models.DateField(null=True, blank=True)
	Num_C11=models.CharField(max_length=30,blank=True, null=True)
	Date_C11=models.DateField(null=True, blank=True)

	def __str__(self):
		return self.Num_Serie
	def Type(self):
		return self.Type_Materiel_FK
	def Service(self):
		return self.Service_FK
	def Etat(self):
		return self.Etat_FK
	class Meta:
		verbose_name_plural = "Materiels"

class Doc_Matr(models.Model):
	Materiel_FK=models.ForeignKey(Materiel,on_delete=models.CASCADE)
	Document_FK=models.ForeignKey(Document,on_delete=models.CASCADE)
	def __str__(self):
		template = '{0.Materiel_FK}      | Document : {0.Document_FK}'
		return template.format(self)
	class Meta:
		verbose_name_plural = "documents des materiels"
