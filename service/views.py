from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import AppointmentDetail, PrescriptionData, PackageData, UserProfile
from django.template import loader
from .forms import AppointmentForm, PrescriptionForm, PackageForm, UserprofileForm
# Create your views here.

def home(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		return render(request, 'service/index.html', {'userdata' : userdata,})

def login_user(request):
	if not request.user.is_authenticated():
		if request.method == "POST":
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					userdata = UserProfile.objects.filter(user = request.user)
					return render(request, 'service/index.html', {'userdata' : userdata,})
				else:
					return render(request, 'service/login.html', {'error_message': 'Your account has been disabled'})
			else:
				return render(request, 'service/login.html', {'error_message': 'Invalid login'})
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		return render(request, 'service/index.html', {'userdata' : userdata,})


def logout_user(request):
	logout(request)
	#form = UserForm(request.POST or None)
	#context = {
	#	"form": form,
	#}
	return render(request, 'service/login.html')


def add_appointment(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		form = AppointmentForm(request.POST or None)
		if form.is_valid():
			appointment1 = form.save(commit=False)
			appointment1.user = request.user
			appointment1.save()
			all_appointment = AppointmentDetail.objects.filter(user = request.user)
			return render(request,'service/appointment.html', {'all_appointment' : all_appointment, 'userdata' : userdata,})
		return render(request, 'service/add_appointment.html', {'form': form,  'userdata' : userdata,})


def appointment(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		all_appointment = AppointmentDetail.objects.filter(user = request.user)
		return render(request,'service/appointment.html', {'all_appointment' : all_appointment, 'userdata' : userdata,})


def add_prescription(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		form = PrescriptionForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			prescription1 = form.save(commit=False)
			prescription1.user = request.user
			prescription1.save()
			all_prescriptions = PrescriptionData.objects.filter(user = request.user)
			return render(request,'service/prescription.html', {'all_prescriptions' : all_prescriptions,'userdata' : userdata,})
		return render(request, 'service/add_prescription.html', {'form': form, 'userdata' : userdata,})

def prescription(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		all_prescriptions = PrescriptionData.objects.filter(user = request.user)
		return render(request,'service/prescription.html', {'all_prescriptions' : all_prescriptions, 'userdata' : userdata,})

def package(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		all_packages = PackageData.objects.filter(user = request.user)
		return render(request,'service/package.html', {'all_packages' : all_packages, 'userdata' : userdata,})

def add_package(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		form = PackageForm(request.POST or None)
		if form.is_valid():
			package1 = form.save(commit=False)
			package1.user = request.user
			package1.save()
			all_packages = PackageData.objects.filter(user = request.user)
			return render(request,'service/package.html', {'all_packages' : all_packages, 'userdata' : userdata,})
		return render(request, 'service/add_package.html', {'form': form, 'userdata' : userdata,})

def user_detail(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		return render(request,'service/user.html', {'userdata' : userdata,})

def edit_user(request, id=None):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.get(user__id=id)
		if request.POST :
			form = UserprofileForm(request.POST, instance = userdata)
			#import ipdb;ipdb.set_trace()
			if form.is_valid():
				#import ipdb;ipdb.set_trace()
				pkt1 = form.save(commit=False)
				pkt1.user = request.user
				pkt1.save()
				userd = UserProfile.objects.filter(user__id=id)
				return render(request,'service/user.html', {'userdata' : userd,})
			return render(request,'service/useredit.html', {'form' : form, 'userdata' : userdata,})
		else:
			userdata = UserProfile.objects.filter(user = request.user)
			form = UserprofileForm(request.POST or None)
			if form.is_valid():
				pkt1 = form.save(commit=False)
				pkt1.user = request.user
				pkt1.save()
				userd = UserProfile.objects.filter(user = request.user)
				return render(request,'service/user.html', {'userdata' : userd,})
			return render(request,'service/useredit.html', {'form' : form, 'userdata' : userdata,})
