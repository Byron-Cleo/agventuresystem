# Generated by Django 2.2 on 2020-01-18 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmcontractmodel',
            name='delivery_period',
            field=models.CharField(default='Delivery Period', max_length=254, verbose_name='Delivery Period'),
        ),
        migrations.AddField(
            model_name='farmcontractmodel',
            name='weighing_conditions',
            field=models.TextField(blank=True, default='', verbose_name='Weighing Conditions'),
        ),
    ]
