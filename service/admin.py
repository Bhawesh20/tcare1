from django.contrib import admin
from .models import AppointmentDetail, PrescriptionData, PackageData, UserProfile
# Register your models here.
admin.site.register(AppointmentDetail)
admin.site.register(PrescriptionData)
admin.site.register(PackageData)
admin.site.register(UserProfile)

