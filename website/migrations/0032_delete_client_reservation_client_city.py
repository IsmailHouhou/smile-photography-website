# Generated by Django 4.1.6 on 2023-02-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0031_remove_message_client_remove_reservation_client_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Client",
        ),
        migrations.AddField(
            model_name="reservation",
            name="client_city",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
