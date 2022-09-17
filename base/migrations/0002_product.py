# Generated by Django 4.1 on 2022-08-04 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.TextField()),
                ('quantity', models.IntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.factory')),
            ],
        ),
    ]
