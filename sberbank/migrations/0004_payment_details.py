# Generated by Django 3.1.7 on 2021-04-01 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sberbank', '0003_auto_20210402_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='details',
            field=models.JSONField(blank=True, null=True, verbose_name='details'),
        ),
    ]