from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PatientRegisterView.as_view(), name='patient_register'),
    path('add/', views.PatientCreateView.as_view(), name='patient_create'),
    path('doctor-consultation/<shortuuid:patient_uuid>/', views.PatientDoctorUpdateView.as_view(),
         name='patient_consultation_update'),
    path('lab-test/<shortuuid:patient_uuid>/', views.PatientLabTestUpdateView.as_view(),
         name='patient_test_result_update'),
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
    path('patients/pending/lab-tests/', views.PendingLabTestListView.as_view(), name='pending_lab_test_list'),
    path('patients/pending/treatment/', views.PendingTreatmentListView.as_view(), name='pending_treatment_list'),
]
