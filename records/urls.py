from django.urls import path, include
from . import views
urlpatterns = [
    path('create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('doctor-consultation/<shortuuid:patient_uuid>/', views.PatientDoctorUpdateView.as_view(),
         name='patient_consultation_update'),
    path('lab-test/<shortuuid:patient_uuid>/', views.PatientLabTestUpdateView.as_view(),
         name='patient_test_result_update'),
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
]
