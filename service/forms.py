from django import forms
from django.contrib.auth.models import Permission, User
from .models import AppointmentDetail, PrescriptionData, PackageData, UserProfile


class DateInput(forms.DateInput):
	input_type = 'date'

class AppointmentForm(forms.ModelForm):

	class Meta:
		model = AppointmentDetail
		fields = ['patient_name', 'phone_number', 'service_required','appointment_date',]
		widgets = {
			'appointment_date': DateInput(),
		}

class PrescriptionForm(forms.ModelForm):

	class Meta:
		model = PrescriptionData
		fields = ['patient_name', 'prescribed_by', 'prescription_date', 'prescription_image' ]
		widgets = {
			'prescription_date': DateInput(),
		}

class PackageForm(forms.ModelForm):
	class Meta:
		model = PackageData
		fields = ['patient_name', 'phone_number', 'service_required', 'duration', 'period']

class UserprofileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['gender', 'contact_number', 'age', 'address']