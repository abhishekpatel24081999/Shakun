# Generated by Django 3.0.4 on 2020-03-21 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Owner', '0005_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='Enter Address')),
                ('village', models.CharField(max_length=50, verbose_name='Enter Village Name')),
                ('city', models.CharField(max_length=50, verbose_name='Enter City Name')),
                ('pin', models.PositiveSmallIntegerField(verbose_name='Enter PinCode No.')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Select User')),
            ],
        ),
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_date', models.DateField(verbose_name='Unaviable Date')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50, verbose_name='Enter First Name')),
                ('lname', models.CharField(max_length=50, verbose_name='Enter Last Name')),
                ('img', models.ImageField(upload_to='user', verbose_name='Insert Image')),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Owner.Product', verbose_name='Select Product')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Select User')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(verbose_name='Enter Appointment Date')),
                ('payment_status', models.BooleanField(verbose_name='Payment Status')),
                ('address', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Customer.Address', verbose_name='Select Address')),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Owner.Product', verbose_name='Select Product')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Select User')),
            ],
        ),
    ]
