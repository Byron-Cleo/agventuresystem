# Generated by Django 2.2 on 2020-01-17 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('farms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerContractModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(default='Agventure Ltd.', max_length=254, verbose_name='Agventure Ltd. (Seller)')),
                ('cust_contract_code', models.CharField(default='', max_length=254, verbose_name='Customer Contract Code')),
                ('agv_kg_price', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='AGV Price/KG (KSH)')),
                ('agv_bag_price', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='AGV Price/Bag (KSh)')),
                ('cust_tolerance', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='Cust. Contract Tolerance +/-')),
                ('delivery_period', models.CharField(default='Delivery Period', max_length=254, verbose_name='Delivery Period')),
                ('quality_specs', models.CharField(default='', max_length=254, verbose_name='Crop Quality Specifications')),
                ('delivery_terms', models.TextField(default='Transport Details to be supplied One Day in Advance by Buyer....', max_length=254, verbose_name='Delivery Terms')),
                ('offloading_fees', models.TextField(blank=True, default='No Offloading Fees for Vehicles are to be Levied by the Buyer', verbose_name='Offloading Fees')),
                ('other_conditions', models.TextField(blank=True, default='', verbose_name='Other Conditions')),
                ('governing_terms', models.TextField(blank=True, default='Kenyan Law Shall Apply', verbose_name='Governing Terms')),
                ('whole_agreement', models.TextField(blank=True, default='', verbose_name='Whole Agreement')),
                ('rejection_procedure', models.TextField(blank=True, default='Rejection can take place at the Farm. Once Accepted and Carried, no Rejection can Take Place. ', verbose_name='Rejection Procedure')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_contract_creator', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_contract', to='customers.CustomerModel', verbose_name='Customer (Buyer)FK')),
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cust_contracts', to='farms.FarmModel')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_contract_updater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
