from django.contrib import admin
from . import models


# 'first_name',
# 'last_name',
# 'middle_name',
# 'date_of_birth',
# 'patient_id_number',
# # 'ward',
# 'signs_and_symptoms',
# 'test',
# 'test_result',
# # Register your models here.
class RecordAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'patient_id_number', 'date_of_birth', 'ward', 'age', 'signs_and_symptoms', 'test', 'test_result', 'treatment')
    list_display_links = ('full_name',)

    search_fields = ('first_name', 'last_name', 'full_name', 'patient_id_number',)

    list_filter = ('ward', 'date_of_birth',)

    fieldsets = (
        ('Personal Information', {
            'fields': (
                'first_name',
                'last_name',
                'middle_name',
                'date_of_birth',
                'patient_id_number',
                'ward',
            )
        }),
        ('Doctor Information', {
            'fields': (
                'signs_and_symptoms',
                'test',
            )
        }),
        ('Lab Information', {
            'fields': (
                'test_result',
            )
        }),
        ('Treatment Information', {
            'fields': (
                'treatment',
            )
        }),
    )

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return False


admin.site.register(models.PatientRecord, RecordAdmin)
