# Generated by Django 3.1.3 on 2020-12-31 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0007_auto_20201231_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlines',
            name='product_qty',
            field=models.FloatField(),
        ),
    ]