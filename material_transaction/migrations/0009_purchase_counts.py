# Generated by Django 2.1.5 on 2019-02-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_transaction', '0008_auto_20190220_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='counts',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
    ]
