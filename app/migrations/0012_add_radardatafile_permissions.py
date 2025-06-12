from django.db import migrations
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def add_radardatafile_permissions(apps, schema_editor):
    RadarDataFile = apps.get_model('app', 'RadarDataFile')
    content_type = ContentType.objects.get_for_model(RadarDataFile)
    
    Permission.objects.get_or_create(
        codename='view_radardatafile',
        name='Can view radar data file',
        content_type=content_type,
    )
    Permission.objects.get_or_create(
        codename='delete_radardatafile',
        name='Can delete radar data file',
        content_type=content_type,
    )

def remove_radardatafile_permissions(apps, schema_editor):
    RadarDataFile = apps.get_model('app', 'RadarDataFile')
    content_type = ContentType.objects.get_for_model(RadarDataFile)
    Permission.objects.filter(content_type=content_type).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('app', '0011_radardatafile'),
    ]

    operations = [
        migrations.RunPython(add_radardatafile_permissions, remove_radardatafile_permissions),
    ] 