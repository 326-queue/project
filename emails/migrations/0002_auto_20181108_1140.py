# Generated by Django 2.1.3 on 2018-11-08 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='time_scheduled',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='email',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('sent', 'Sent'), ('scheduled', 'Scheduled')], max_length=10),
        ),
        migrations.AlterField(
            model_name='email',
            name='time_sent',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
