# Generated by Django 5.0.3 on 2024-04-03 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_batiment_surface"),
    ]

    operations = [
        migrations.AlterField(
            model_name="batiment",
            name="usage",
            field=models.IntegerField(default=None),
        ),
    ]
