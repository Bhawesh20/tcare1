from django.db import models
# Create your models here.
from django.contrib.auth.models import User
class UserProfile(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	user = models.OneToOneField(User)
	gender =models.CharField(max_length=10, choices=GENDER_CHOICES, default = 'M')
	profile_photo = models.ImageField()
	contact_number = models.IntegerField()
	age = models.PositiveIntegerField()
	address = models.CharField(max_length=1000)
	def __str__(self):
		return str(self.pk) + ' ' +self.user.username



class AppointmentDetail(models.Model):
	user = models.ForeignKey(User, default=1)
	MALENURSE = 'Male Nurse'
	FEMALENURSE = 'Female Nurse'
	BABYSITTER = 'Baby Sitter'
	PHYSIOTHERAPIST = 'Physiotherapist'
	service_choices = (
		(MALENURSE, 'Male Nurse'),
		(FEMALENURSE, 'Female Nurse'),
		(BABYSITTER, 'Babysitter'),
		(PHYSIOTHERAPIST, 'physiotherapist'),
		)

	patient_name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=10, default= None)
	service_required = models.CharField(max_length=20, choices = service_choices, default = MALENURSE)
	served_by = models.CharField(max_length=50, default='Unassigned')
	appointment_date = models.DateField(auto_now=False, auto_now_add=False)
	status = models.CharField(max_length=50, default='Pending')

	def __str__(self):
		return str(self.pk) +'. Patient: ' + self.patient_name +' -->Service Required:' + self.service_required

class PrescriptionData(models.Model):
	user = models.ForeignKey(User, default=1)
	patient_name = models.CharField(max_length=50)
	prescribed_by = models.CharField(max_length=50)
	prescription_date = models.DateField(auto_now=False, auto_now_add=False)
	prescription_image = models.ImageField()

	def __str__(self):
		return str(self.pk)+ '. Patient: ' + self.patient_name + '  Prescribed_by: ' + self.prescribed_by

#class LabtestData(models.Model):
#	test_choices = (
#		('Complete Blood Count', 'Complete Blood Count'),
	#	('Fast Blood Sugar', 'Fast Blood Sugar'),
	#	('Postprandial Blood Sugar', 'Postprandial Blood Sugar'),
	#	('Lipid Profile', 'Lipid Profile'),
	#	('Uric Acid', 'Uric Acid'),
	#	('Blood Pressure Test', 'Blood Pressure Test'),
	#	)
#	patient_name = models.CharField(max_length=50)
#	test_type = models.CharField(max_length=30, choices=test_choices, default = ' ')
#	test_date = models.DateField(auto_now=False, auto_now_add=False)
#	status = models.CharField(max_length=50, default='Pending')
#
#	def __str__(self):
#		return str(self.pk)+ '. Patient: ' + self.patient_name + '  Test type: ' + self.test_type

class PackageData(models.Model):
	user = models.ForeignKey(User, default=1)
	servicetype_choice = (
		('MN', 'Male Nurse'),
		('FN', 'Female Nurse'),
		('BS', 'Babysitter'),
		('PS', 'Physiotherapist'),
		)
	duration_choice = (
		('8hrs', '8hrs/day'),
		('12hrs', '12hrs/day'),
		('16hrs', '16hrs/day'),
		('24hrs', '24hrs/day'),
		)
	period_choice = (
		('7day', '7days'),
		('15day', '15days'),
		('30day', '30days'),
		)
	patient_name = models.CharField(max_length=50)
	phone_number = models.IntegerField()
	service_required = models.CharField(max_length=20, choices = servicetype_choice, default = ' ')
	duration = models.CharField(max_length=20, choices = duration_choice, default = ' ')
	period = models.CharField(max_length=20, choices = period_choice, default = ' ')
	status = models.CharField(max_length=50, default='Pending')
	def __str__(self):
		return str(self.pk)+ '. Patient: ' + self.patient_name + '  Prescribed_by: ' + self.service_required