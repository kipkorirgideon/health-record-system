from algoliasearch_django.decorators import register
from algoliasearch_django import AlgoliaIndex

from .models import Patient


@register(Patient)
class PatientIndex(AlgoliaIndex):
    should_index = 'is_active'
    custom_objectID = 'uuid'
    fields = ('uuid', 'patient_id_number', 'first_name', 'last_name', 'patient_id_number', 'age', 'ward')
    settings = {
        'searchableAttributes': ['patient_id_number', 'first_name', 'last_name', 'ward'],
        'attributesForFaceting': ['searchable(ward)', 'age'],
    }
