# Generated by Django 5.0.2 on 2025-06-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_radarconfig_direction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='radarobjectdetection',
            name='direction_name',
            field=models.CharField(blank=True, help_text='Direction name for this detection', max_length=100, null=True),
        ),
    ]
