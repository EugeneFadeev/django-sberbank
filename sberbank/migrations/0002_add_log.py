# Generated by Django 3.1.7 on 2021-04-01 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sberbank', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logentry',
            options={'ordering': ['-created'], 'verbose_name': 'запись в журнале', 'verbose_name_plural': 'записи в журнале'},
        ),
    ]