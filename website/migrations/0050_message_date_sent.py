# Generated by Django 4.1.6 on 2023-03-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0049_remove_message_date_sent_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="date_sent",
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]