# Generated by Django 4.1.7 on 2023-03-17 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Fecha de envio"
            ),
        ),
    ]
