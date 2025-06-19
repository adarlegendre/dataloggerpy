from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_radarobjectdetection_direction_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='radardatafile',
            name='email_sent',
            field=models.BooleanField(default=False, help_text='Whether this file has been sent via email'),
        ),
    ] 