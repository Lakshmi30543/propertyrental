# Generated by Django 5.0.7 on 2024-12-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0030_alter_ownerprofile_options_ownerprofile_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerprofile',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Enter your contact number', max_length=10, null=True),
        ),
    ]
