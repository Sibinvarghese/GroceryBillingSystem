# Generated by Django 3.1.3 on 2020-12-30 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_auto_20201230_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='bill_total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='orderlines',
            name='amount',
            field=models.FloatField(),
        ),
    ]
