# Generated by Django 2.2 on 2019-04-01 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemmatized_text', '0005_auto_20190312_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='lemmatizedtext',
            name='completed',
            field=models.IntegerField(default=0),
        ),
    ]
