from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_anprconfig_radar'),
    ]

    operations = [
        migrations.AddField(
            model_name='radarobjectdetection',
            name='email_sent',
            field=models.BooleanField(default=False, help_text='Whether notification email has been sent'),
        ),
        migrations.CreateModel(
            name='EmailNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(help_text='Start date of the detection period')),
                ('end_date', models.DateTimeField(help_text='End date of the detection period')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('sent', 'Sent'), ('failed', 'Failed')], default='pending', max_length=10)),
                ('error_message', models.TextField(blank=True, help_text='Error message if sending failed', null=True)),
                ('sent_at', models.DateTimeField(blank=True, help_text='When the email was sent', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('notification_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.notificationsettings')),
            ],
            options={
                'verbose_name': 'Email Notification',
                'verbose_name_plural': 'Email Notifications',
                'ordering': ['-created_at'],
                'indexes': [
                    models.Index(fields=['status', 'created_at'], name='email_notif_status_created_idx'),
                ],
            },
        ),
    ] 