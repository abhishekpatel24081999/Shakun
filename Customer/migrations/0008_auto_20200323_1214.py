# Generated by Django 3.0.4 on 2020-03-23 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0007_auto_20200322_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Time',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Conform ?'),
        ),
    ]
