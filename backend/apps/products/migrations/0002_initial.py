# Generated by Django 5.1.4 on 2025-04-12 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend_products', '0001_initial'),
        ('backend_vendors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_vendors.vendor'),
        ),
    ]
