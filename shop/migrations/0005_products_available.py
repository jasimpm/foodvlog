# Generated by Django 2.2 on 2022-01-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_products_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
