# Generated by Django 3.0.4 on 2020-03-22 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0004_auto_20200322_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='pin',
            field=models.PositiveIntegerField(verbose_name='Enter PinCode No.'),
        ),
    ]