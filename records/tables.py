import django_tables2 as tables
from . import models


class PatientTable(tables.Table):
    class Meta:
        model = models.Patient
        template_name = "django_tables2/bootstrap.html"
        fields = ("patient_id_number", "first_name", "last_name",)
        attr = {
            "class": "table table-striped",
        }
        template_name = "django_tables2/bootstrap4.html"
