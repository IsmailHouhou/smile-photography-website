# Generated by Django 4.1.6 on 2023-02-21 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0011_alter_message_date_sent"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="date_sent",
        ),
    ]