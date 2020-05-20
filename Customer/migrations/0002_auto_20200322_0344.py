# Generated by Django 3.0.4 on 2020-03-21 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Enter City Name')),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.City', verbose_name='Select City'),
        ),
    ]
