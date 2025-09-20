from django.shortcuts import render

# Create your views here.
# main_app/views.py

from django.http import JsonResponse
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from .models import PatientProfile, DoctorProfile, MedicalHistory, Prescription, Bill
import json
from datetime import datetime

User = get_user_model()

@csrf_exempt
def create_patient(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create_user(username=data['username'], password=data['password'], user_type=3)
        patient_profile = PatientProfile.objects.create(user=user, age=data['age'], address=data['address'])
        return JsonResponse({'message': 'Patient created successfully', 'id': user.id})

@csrf_exempt
def create_doctor(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create_user(username=data['username'], password=data['password'], user_type=2)
        doctor_profile = DoctorProfile.objects.create(user=user, specialization=data['specialization'])
        return JsonResponse({'message': 'Doctor created successfully', 'id': user.id})

def list_patients(request):
    patients = PatientProfile.objects.all()
    result = []
    for patient in patients:
        result.append({
            'id': patient.user.id,
            'username': patient.user.username,
            'age': patient.age,
            'address': patient.address
        })
    return JsonResponse(result, safe=False)

def get_patient_history(request, patient_id):
    histories = MedicalHistory.objects.filter(patient_id=patient_id)
    result = []
    for history in histories:
        result.append({
            'id': history.id,
            'description': history.description,
            'date': history.date.strftime('%Y-%m-%d')
        })
    return JsonResponse(result, safe=False)

def get_prescriptions(request, patient_id):
    prescriptions = Prescription.objects.filter(patient_id=patient_id)
    result = []
    for pres in prescriptions:
        result.append({
            'id': pres.id,
            'doctor': pres.doctor.user.username,
            'medicine_details': pres.medicine_details,
            'date': pres.date.strftime('%Y-%m-%d')
        })
    return JsonResponse(result, safe=False)

def get_bills(request, patient_id):
    bills = Bill.objects.filter(patient_id=patient_id)
    result = []
    for bill in bills:
        result.append({
            'id': bill.id,
            'amount': str(bill.amount),
            'date': bill.date.strftime('%Y-%m-%d'),
            'details': bill.details
        })
    return JsonResponse(result, safe=False)

@csrf_exempt
def add_medical_history(request, patient_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        patient = PatientProfile.objects.get(user_id=patient_id)
        history = MedicalHistory.objects.create(
            patient=patient,
            description=data['description'],
            date=datetime.strptime(data['date'], '%Y-%m-%d').date()
        )
        return JsonResponse({'message': 'Medical history added', 'id': history.id})

@csrf_exempt
def add_prescription(request, patient_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        patient = PatientProfile.objects.get(user_id=patient_id)
        doctor = DoctorProfile.objects.get(user_id=data['doctor_id'])
        pres = Prescription.objects.create(
            patient=patient,
            doctor=doctor,
            medicine_details=data['medicine_details'],
            date=datetime.strptime(data['date'], '%Y-%m-%d').date()
        )
        return JsonResponse({'message': 'Prescription added', 'id': pres.id})

@csrf_exempt
def add_bill(request, patient_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        patient = PatientProfile.objects.get(user_id=patient_id)
        bill = Bill.objects.create(
            patient=patient,
            amount=data['amount'],
            date=datetime.strptime(data['date'], '%Y-%m-%d').date(),
            details=data['details']
        )
        return JsonResponse({'message': 'Bill added', 'id': bill.id})

