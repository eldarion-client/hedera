# Generated by Django 2.2 on 2019-04-04 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lemmatized_text', '0006_lemmatizedtext_completed'),
        ('vocab_list', '0005_auto_20190401_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalVocabularyStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unranked', models.DecimalField(decimal_places=2, default='0', max_digits=5)),
                ('one', models.DecimalField(decimal_places=2, default='0', max_digits=5)),
                ('two', models.DecimalField(decimal_places=2, default='0', max_digits=5)),
                ('three', models.DecimalField(decimal_places=2, default='0', max_digits=5)),
                ('four', models.DecimalField(decimal_places=2, default='0', max_digits=5)),
                ('five', models.DecimalField(decimal_places=2, default='0', max_digits=5)),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lemmatized_text.LemmatizedText')),
                ('vocab_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocab_list.PersonalVocabularyList')),
            ],
        ),
    ]
