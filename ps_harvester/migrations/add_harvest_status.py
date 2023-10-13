# Generated by Django 4.2.5 on 2023-10-13 15:49

from django.db import migrations


def initiate_status(apps, schema_editor):

    harvest_status = apps.get_model('ps_harvester', 'HarvestStatus')
    
    initial_status = [
        (1, 'COMPLETE'),
        (2, 'INCOMPLETE'),
        (3, 'PENDING REVIEW'),
        (4, 'ERROR')
    ]
    
    for status_id, status_name in initial_status:
        harvest_status.objects.create(status_id=status_id, status_name=status_name)


class Migration(migrations.Migration):

    dependencies = [
        ('ps_harvester','0001_initial')
    ]

    operations = [
        migrations.RunPython(initiate_status)
    ]
