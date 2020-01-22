# Generated by Django 2.2 on 2020-01-19 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer_interests', '0002_auto_20200119_1908'),
        ('farms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPaymentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_paid', models.CharField(choices=[('', 'Specify Bank of Customer Payment'), ('1', 'NCBA Bank - Acc. 6680660011'), ('2', 'Victoria Commercial Bank - Acc. 1008260016')], default='', max_length=254)),
                ('amount_payable', models.DecimalField(decimal_places=4, default=0.0, max_digits=20)),
                ('pay_reference', models.CharField(default='', max_length=254)),
                ('payment_status', models.CharField(choices=[('', 'Specify Customer Order if Paid or Not Paid'), ('1', 'Order Paid (Confirmed)'), ('2', 'Order Not Paid')], default='', max_length=254)),
                ('order_paid_by', models.CharField(default='', max_length=254)),
                ('payment_terms', models.CharField(choices=[('', 'Specify Customer Order if Paid or Not Paid'), ('1', 'Cash'), ('2', 'Pre-Paid'), ('3', 'Payment after 30 Days'), ('4', 'Payment after 60 Days')], default='', max_length=254)),
                ('date_overdue', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_payment_creator', to=settings.AUTH_USER_MODEL)),
                ('customer_interest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_interest_payment', to='customer_interests.CustomerInterestModel')),
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='farms.FarmModel')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_payment_updater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]