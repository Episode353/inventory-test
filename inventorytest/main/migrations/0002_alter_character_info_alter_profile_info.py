# Generated by Django 5.0 on 2024-07-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='info',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='profile',
            name='info',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
