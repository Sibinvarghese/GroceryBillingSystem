# Generated by Django 3.1.3 on 2020-12-30 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_auto_20201230_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlines',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.product'),
        ),
    ]