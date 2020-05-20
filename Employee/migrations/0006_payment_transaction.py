# Generated by Django 3.0.4 on 2020-04-04 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0016_auto_20200401_2311'),
        ('Employee', '0005_manageappointment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.PositiveIntegerField(verbose_name='Enter Total Amount')),
                ('paied_amount', models.PositiveIntegerField(verbose_name='Paied Amount:-')),
                ('c_able', models.BooleanField(default=False, verbose_name='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Customer.Appointment', verbose_name='Select Appointment:-')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TXNID', models.CharField(max_length=150, verbose_name='Trasiction ID')),
                ('TXNAMOUNT', models.FloatField(verbose_name='Transicton Amount')),
                ('PAYMENTMODE', models.CharField(max_length=50, verbose_name='Payment Mode')),
                ('CURRENCY', models.CharField(max_length=50, verbose_name='Currency of payment mode')),
                ('STATUS', models.BooleanField(default=False, verbose_name='Payment Status')),
                ('GATEWAYMODE', models.CharField(max_length=50, verbose_name='Gateway Mode')),
                ('BANKTXNID', models.CharField(max_length=50, verbose_name='Bank ID')),
                ('BANKNAME', models.CharField(max_length=50, verbose_name='Bank Name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.Payment', verbose_name='Payment ID')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]