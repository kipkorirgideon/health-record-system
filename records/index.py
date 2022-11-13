from algoliasearch_django.decorators import register
from algoliasearch_django import AlgoliaIndex

from .models import Patient


@register(Patient)
class PatientIndex(AlgoliaIndex):
    should_index = 'is_active'
    custom_objectID = 'id'
    fields = ('patient_id_number', 'first_name', 'last_name', 'middle_name', 'date_of_birth', 'patient_id_number')
    settings = {
        'searchableAttributes': ['first_name', 'last_name', 'email'],
        'attributesForFaceting': ['first_name', 'last_name', 'email'],
    }
