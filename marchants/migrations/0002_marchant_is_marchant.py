# Generated by Django 2.2.17 on 2020-11-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marchants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marchant',
            name='is_marchant',
            field=models.BooleanField(default=False),
        ),
    ]
