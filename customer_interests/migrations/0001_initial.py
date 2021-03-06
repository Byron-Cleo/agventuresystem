# Generated by Django 2.2 on 2020-01-17 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('crop_stocks', '0001_initial'),
        ('farms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInterestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.CharField(choices=[('', 'Specify Supply Order in Bulk/Bags'), ('1', 'Bulk Order'), ('2', 'Bags Order')], default='', max_length=254, verbose_name='Order Type')),
                ('bag_type', models.CharField(choices=[('', 'Specify Interested Bag Type'), ('1', '90 KG'), ('2', '50 KG')], default=1, max_length=254, verbose_name='Customer Bag Type')),
                ('ordered_quantity', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='Max. Ordered Quantity (KGs)')),
                ('cust_kg_price', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='Customer Price/KG (KSh)')),
                ('farm_kg_price', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='Farm Price/KG (Ksh)')),
                ('cust_bag_price', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='Customer Bag/KG (KSh)')),
                ('farm_bag_price', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='Farm Price/Bag (Ksh)')),
                ('total_bags', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='Total Bags')),
                ('farm_approval', models.CharField(choices=[('', 'Please Approve/Disapprove the Cust. Order'), ('1', 'Order Approved'), ('2', 'Order Not Approved')], default='', max_length=254, verbose_name='Farm App/Disapp.')),
                ('payment_terms', models.CharField(choices=[('', 'Specify Customer Payment Terms '), ('1', 'Cash'), ('2', 'Pre-Paid'), ('3', 'Payment after 30 Days'), ('4', 'Payment after 60 Days')], default='', max_length=254, verbose_name='Payment Terms')),
                ('cust_dest', models.CharField(default='', max_length=254, verbose_name='Customer Destination')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interest_creator', to=settings.AUTH_USER_MODEL)),
                ('crop_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_interests', to='crop_stocks.CropStockModel', verbose_name='Crop of Interest/Order')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_orders', to='customers.CustomerModel', verbose_name='Customer Name')),
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='farms.FarmModel')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interest_updater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
