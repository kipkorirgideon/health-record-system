# Generated by Django 4.1.3 on 2022-11-13 23:22

from django.db import migrations
import native_shortuuid.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_historicaluser_username_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='uuid',
            field=native_shortuuid.fields.NativeShortUUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=native_shortuuid.fields.NativeShortUUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
