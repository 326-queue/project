# Generated by Django 2.1.3 on 2018-11-28 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsorship',
            old_name='tier',
            new_name='tiers',
        ),
    ]