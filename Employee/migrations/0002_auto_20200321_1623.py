# Generated by Django 3.0.4 on 2020-03-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='employee', verbose_name='Insert Image'),
        ),
    ]