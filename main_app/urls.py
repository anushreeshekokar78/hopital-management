# main_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.list_patients),
    path('patients/create/', views.create_patient),
    path('doctors/create/', views.create_doctor),
    path('patients/<int:patient_id>/history/', views.get_patient_history),
    path('patients/<int:patient_id>/prescriptions/', views.get_prescriptions),
    path('patients/<int:patient_id>/bills/', views.get_bills),
    path('patients/<int:patient_id>/history/add/', views.add_medical_history),
    path('patients/<int:patient_id>/prescriptions/add/', views.add_prescription),
    path('patients/<int:patient_id>/bills/add/', views.add_bill),
]
