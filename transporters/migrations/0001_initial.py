# Generated by Django 2.2 on 2020-01-19 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TransportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=254, verbose_name='Transporter Name')),
                ('contract_status', models.CharField(choices=[('', 'Specify if the Transporter is Still Working with Agventure Ltd'), ('active', 'Active'), ('not active', 'Not Active')], default='', max_length=254, verbose_name='AGV-Transporter Contract Status')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transporter_creator', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transporter_updater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
