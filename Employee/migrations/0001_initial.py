# Generated by Django 3.0.4 on 2020-03-21 10:10

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
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50, verbose_name='Enter First Name')),
                ('lname', models.CharField(max_length=50, verbose_name='Enter Last Name')),
                ('img', models.ImageField(upload_to='employee', verbose_name='Insert Image')),
                ('contact', models.PositiveIntegerField(default=0)),
                ('email', models.EmailField(default=0, max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Select User')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
