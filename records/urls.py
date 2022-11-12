from django.urls import path, include
from . import views
urlpatterns = [
    path('create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('doctor_update/<int:patient_id>/', views.PatientDoctorUpdateView.as_view(), name='patient_doctor_update'),
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
]
