# Generated by Django 2.1.3 on 2018-11-27 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0002_auto_20181108_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField(blank=True)),
                ('fundraising_goal', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perks', to='hackathons.Hackathon')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution', models.IntegerField()),
                ('status', models.CharField(choices=[('uncontacted', 'Uncontacted'), ('contacted', 'Contacted'), ('donated', 'Donated')], max_length=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsorships', to='companies.Company')),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsorships', to='hackathons.Hackathon')),
                ('perks', models.ManyToManyField(blank=True, to='hackathons.Perk')),
            ],
        ),
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tiers', to='hackathons.Hackathon')),
            ],
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='tier',
            field=models.ManyToManyField(blank=True, to='hackathons.Tier'),
        ),
    ]