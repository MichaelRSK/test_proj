# Generated by Django 4.2.9 on 2024-03-12 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='media_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='media',
            old_name='media_url',
            new_name='url',
        ),
    ]
