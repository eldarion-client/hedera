# Generated by Django 2.2.13 on 2020-07-26 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20200726_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_classes', to=settings.AUTH_USER_MODEL),
        ),
    ]
