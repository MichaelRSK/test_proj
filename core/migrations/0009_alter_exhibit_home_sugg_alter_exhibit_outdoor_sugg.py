# Generated by Django 4.2.9 on 2024-03-12 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_data_created_data_updated_exhibit_home_sugg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='home_sugg',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='outdoor_sugg',
            field=models.TextField(blank=True, null=True),
        ),
    ]
