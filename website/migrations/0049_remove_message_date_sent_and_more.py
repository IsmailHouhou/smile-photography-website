# Generated by Django 4.1.6 on 2023-03-12 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0048_alter_video_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="date_sent",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="order_date",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="order_hour",
        ),
        migrations.AddField(
            model_name="reservation",
            name="order_date_time",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
