# Generated by Django 5.2.3 on 2025-06-11 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cat_api.cat'),
        ),
    ]
