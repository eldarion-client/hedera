# Generated by Django 2.2.6 on 2019-10-18 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lattices', '0002_auto_20190214_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='latticenode',
            name='canonical',
            field=models.BooleanField(default=False),
        ),
    ]