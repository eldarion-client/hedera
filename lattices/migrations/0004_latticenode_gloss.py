# Generated by Django 2.2.6 on 2019-11-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lattices', '0003_latticenode_canonical'),
    ]

    operations = [
        migrations.AddField(
            model_name='latticenode',
            name='gloss',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
