# Generated by Django 4.1.2 on 2022-10-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app4", "0002_person_friendship"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
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
                ("name", models.CharField(max_length=128)),
                (
                    "members",
                    models.ManyToManyField(related_name="groups", to="app4.person"),
                ),
            ],
        ),
    ]
