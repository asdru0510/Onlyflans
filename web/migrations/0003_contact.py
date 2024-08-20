# Generated by Django 5.1 on 2024-08-20 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0002_flan_description_flan_image_url_flan_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("nombre", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=100)),
                ("mensaje", models.TextField(max_length=500)),
            ],
        ),
    ]
