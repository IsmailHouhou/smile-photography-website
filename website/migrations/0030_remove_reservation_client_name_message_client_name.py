# Generated by Django 4.1.6 on 2023-02-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0029_reservation_client_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reservation",
            name="client_name",
        ),
        migrations.AddField(
            model_name="message",
            name="client_name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
