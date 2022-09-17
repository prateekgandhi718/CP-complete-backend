# Generated by Django 4.0.7 on 2022-09-10 10:27

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='posts/default.png', null=True, upload_to=base.models.upload_to, verbose_name='Image'),
        ),
    ]