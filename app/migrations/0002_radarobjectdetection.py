# Generated by Django 5.0.2 on 2025-06-16 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadarObjectDetection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(help_text='When the object was first detected')),
                ('end_time', models.DateTimeField(help_text='When the object was last detected')),
                ('min_range', models.FloatField(help_text='Minimum range during detection (meters)')),
                ('max_range', models.FloatField(help_text='Maximum range during detection (meters)')),
                ('avg_range', models.FloatField(help_text='Average range during detection (meters)')),
                ('min_speed', models.FloatField(help_text='Minimum speed during detection (km/h)')),
                ('max_speed', models.FloatField(help_text='Maximum speed during detection (km/h)')),
                ('avg_speed', models.FloatField(help_text='Average speed during detection (km/h)')),
                ('detection_count', models.IntegerField(help_text='Number of readings in this detection')),
                ('raw_data', models.JSONField(help_text='All raw readings for this detection')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('radar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='object_detections', to='app.radarconfig')),
            ],
            options={
                'verbose_name': 'Radar Object Detection',
                'verbose_name_plural': 'Radar Object Detections',
                'ordering': ['-start_time'],
                'indexes': [models.Index(fields=['radar', 'start_time'], name='app_radarob_radar_i_b4feea_idx'), models.Index(fields=['radar', 'end_time'], name='app_radarob_radar_i_f00f39_idx')],
            },
        ),
    ]
