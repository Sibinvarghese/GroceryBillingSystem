# Generated by Django 3.1.3 on 2020-12-30 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlines',
            name='bill_number',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderLines',
        ),
    ]