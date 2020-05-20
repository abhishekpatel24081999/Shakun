# Generated by Django 3.0.4 on 2020-03-21 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Owner', '0003_auto_20200321_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='status',
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Owner.Owner', verbose_name='Select Owner'),
        ),
    ]
