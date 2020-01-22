# Generated by Django 2.2 on 2020-01-17 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CropStockModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=254, verbose_name='Crop Name')),
                ('code', models.CharField(blank=True, default='', max_length=254, verbose_name='Crop Code')),
                ('variety', models.CharField(blank=True, default='', max_length=254, verbose_name=' Crop Variety')),
                ('grade', models.CharField(blank=True, default='', max_length=254, verbose_name='Crop Grade')),
                ('comment', models.CharField(blank=True, default='', max_length=254, verbose_name='Comment')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='crop_stock_creator', to=settings.AUTH_USER_MODEL)),
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='farms.FarmModel', verbose_name='Farm From')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='crop_stock_update', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
