# Generated by Django 2.2.12 on 2020-06-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='group',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
