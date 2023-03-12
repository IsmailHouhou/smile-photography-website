# Generated by Django 4.1.6 on 2023-03-12 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0046_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="category",
            field=models.CharField(
                choices=[
                    ("Category1", "Category1"),
                    ("Documentary", "Documentary"),
                    ("Advertisement", "Advertisement"),
                    ("Event", "Event"),
                    ("Reporting", "Reporting"),
                ],
                max_length=200,
            ),
        ),
    ]
