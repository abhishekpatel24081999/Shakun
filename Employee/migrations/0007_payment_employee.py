# Generated by Django 3.0.4 on 2020-04-05 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Owner', '0011_auto_20200401_1600'),
        ('Employee', '0006_payment_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='employee',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Owner.Employee', verbose_name='Select Emloyee'),
        ),
    ]
