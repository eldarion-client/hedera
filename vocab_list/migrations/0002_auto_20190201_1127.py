# Generated by Django 2.1.5 on 2019-02-01 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lattices', '__first__'),
        ('vocab_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vocabularylistentry',
            old_name='lemma',
            new_name='headword',
        ),
        migrations.AddField(
            model_name='vocabularylistentry',
            name='node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lattices.LatticeNode'),
        ),
        migrations.AlterUniqueTogether(
            name='vocabularylistentry',
            unique_together={('vocabulary_list', 'headword')},
        ),
    ]
