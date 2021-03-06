# Generated by Django 3.1.3 on 2020-12-30 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20201230_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billnumber', models.CharField(max_length=10, unique=True)),
                ('bill_date', models.DateField(auto_now=True)),
                ('customer_name', models.CharField(max_length=60)),
                ('phone_number', models.CharField(max_length=12)),
                ('bill_total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderLines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=60)),
                ('product_qty', models.FloatField()),
                ('amount', models.FloatField()),
                ('bill_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.order')),
            ],
        ),
    ]
