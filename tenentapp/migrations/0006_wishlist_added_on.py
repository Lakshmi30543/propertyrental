# Generated by Django 5.0.7 on 2024-12-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenentapp', '0005_wishlist_delete_propertywishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
