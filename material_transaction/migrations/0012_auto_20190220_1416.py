# Generated by Django 2.1.5 on 2019-02-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_transaction', '0011_auto_20190220_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='counts',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]