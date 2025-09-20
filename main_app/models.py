from django.db import models

# Create your models here.
# main_app/models.py


from django.contrib.auth.models import AbstractUser

# Custom user model to distinguish between Admin, Doctor, and Patient
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Admin'),
        (2, 'Doctor'),
        (3, 'Patient'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=3)

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.user.username

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class MedicalHistory(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='medical_histories')
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.patient.user.username} - {self.date}"

class Prescription(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='prescriptions')
    medicine_details = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.patient.user.username} - {self.date}"

class Bill(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='bills')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    details = models.TextField()

    def __str__(self):
        return f"{self.patient.user.username} - {self.amount}"
