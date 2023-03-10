# Generated by Django 4.1.6 on 2023-02-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0004_reservation_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="address",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="client",
            name="city",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="client",
            name="region",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="video",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
