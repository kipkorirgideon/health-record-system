from algoliasearch_django.decorators import register
from algoliasearch_django import AlgoliaIndex

from .models import Patient


@register(Patient)
class PatientIndex(AlgoliaIndex):
    should_index = 'is_active'
    custom_objectID = 'uuid'
    fields = ('uuid', 'id', 'patient_id_number', 'first_name', 'last_name','date_of_birth', 'patient_id_number', 'age','ward')
    settings = {
        'searchableAttributes': ['searchable(patient_id_number)', 'searchable(ward)'],
        'attributesForFaceting': ['first_name', 'last_name', 'ward'],
    }
