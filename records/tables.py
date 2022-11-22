import django_tables2 as tables
from . import models


class PatientTable(tables.Table):
    class Meta:
        model = models.Patient
        fields = ("patient_id_number", "first_name", "last_name",)
        attr = {
            "class": "table table-striped",
        }
        template_name = "django_tables2/bootstrap4.html"


class PatientRecordPendingConsultationTable(tables.Table):
    update_btn = tables.Column(
        empty_values=('', 'Update',), verbose_name='Add Consultation', exclude_from_export=True,
        linkify=("patient_consultation_update",  [tables.A("uuid")]), orderable=False, attrs={
            'a': {'class': 'btn btn-primary btn-sm'},
        }
    )

    def render_update_btn(self, record):
        return 'Add Consultation'

    class Meta:
        model = models.PatientRecord
        fields = ("patient_id_number", "first_name", "last_name",)

        attr = {
            "class": "table table-striped",
        }

        template_name = "django_tables2/bootstrap4.html"


class PatientRecordPendingLabTestTable(tables.Table):
    update_btn = tables.Column(
        empty_values=('', 'Update',), verbose_name='Add Lab Test', exclude_from_export=True,
        linkify=("patient_test_result_update",  [tables.A("uuid")]), orderable=False, attrs={
            'a': {'class': 'btn btn-primary btn-sm'},
        }
    )

    def render_update_btn(self, record):
        return 'Add Lab Test'

    class Meta:
        model = models.PatientRecord
        fields = ("patient_id_number", "first_name", "last_name",)

        attr = {
            "class": "table table-striped",
        }

        template_name = "django_tables2/bootstrap4.html"


class PatientRecordPendingTreatmentTable(tables.Table):
    update_btn = tables.Column(
        empty_values=('', 'Update',), verbose_name='Add Treatment', exclude_from_export=True,
        linkify=("add_patient_treatment",  [tables.A("uuid")]), orderable=False, attrs={
            'a': {'class': 'btn btn-primary btn-sm'},
        }
    )

    def render_update_btn(self, record):
        return 'Add Treatment'

    class Meta:
        model = models.PatientRecord
        fields = ("patient_id_number", "first_name", "last_name",)

        attr = {
            "class": "table table-striped",
        }

        template_name = "django_tables2/bootstrap4.html"
