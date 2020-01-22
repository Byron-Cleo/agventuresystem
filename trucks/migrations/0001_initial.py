# Generated by Django 2.2 on 2020-01-20 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transporters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TruckModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_weight', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='Truck Max. Weight(KGs)')),
                ('truck_type', models.CharField(choices=[('', 'Specify Means of Crop Transport'), ('1', 'Truck'), ('2', 'Canter')], default='', max_length=254, verbose_name='Truck Type')),
                ('reg_number', models.CharField(default='', max_length=254, verbose_name='Truck Reg. Number')),
                ('chassis_number', models.CharField(default='', max_length=254, verbose_name='Truck Chassis Number')),
                ('color', models.CharField(default='', max_length=254, verbose_name='Truck Color')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='truck_creator', to=settings.AUTH_USER_MODEL)),
                ('transporter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trucks', to='transporters.TransportModel', verbose_name='Truck Transporter')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='truck_updater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]