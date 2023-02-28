# Generated by Django 4.1.6 on 2023-02-25 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0027_remove_message_client_remove_reservation_client_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("address", models.CharField(blank=True, max_length=200, null=True)),
                ("city", models.CharField(blank=True, max_length=200, null=True)),
                ("region", models.CharField(blank=True, max_length=200, null=True)),
                ("company", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("personal", "personal"),
                            ("business", "business"),
                            ("student", "student"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="message",
            name="client_email",
        ),
        migrations.RemoveField(
            model_name="message",
            name="client_name",
        ),
        migrations.RemoveField(
            model_name="message",
            name="client_phone",
        ),
        migrations.RemoveField(
            model_name="message",
            name="client_prefix",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="client_address",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="client_email",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="client_name",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="client_phone",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="client_prefix",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="client_status",
        ),
        migrations.AddField(
            model_name="message",
            name="client",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="website.client",
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="client",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="website.client",
            ),
        ),
    ]
