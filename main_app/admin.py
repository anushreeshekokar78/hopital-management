

# Register your models here.
# main_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, PatientProfile, DoctorProfile, MedicalHistory, Prescription, Bill

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('User Type', {'fields': ('user_type',)}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(MedicalHistory)
admin.site.register(Prescription)
admin.site.register(Bill)
