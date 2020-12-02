# Generated by Django 2.2.17 on 2020-11-30 13:29

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201130_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='PNG', keep_meta=True, quality=75, size=[312, 312], upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='PNG', keep_meta=True, quality=75, size=[312, 312], upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]