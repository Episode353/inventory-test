# Generated by Django 5.0 on 2024-07-23 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_bundle_description_alter_bundle_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='info',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='info',
        ),
    ]
