# Generated by Django 2.1.5 on 2019-03-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0008_auto_20190307_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='total',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
    ]