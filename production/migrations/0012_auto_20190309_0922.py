# Generated by Django 2.1.5 on 2019-03-09 03:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0011_auto_20190309_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='Order_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]