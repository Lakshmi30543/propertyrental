# Generated by Django 5.0.7 on 2024-12-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0027_property_location_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='location_url',
            field=models.URLField(blank=True, help_text='OpenStreetMap URL for the property location', max_length=500, null=True),
        ),
    ]
