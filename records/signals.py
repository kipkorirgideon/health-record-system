from django.db.models.signals import post_save
from django.dispatch import receiver

from records import models


@receiver(post_save, sender=models.Patient)
def create_patient_record(sender, instance, created, **kwargs):
    if created:
        models.PatientRecord(patient_ptr=instance).save_base(raw=True)

