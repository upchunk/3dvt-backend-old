# Generated by Django 4.1.2 on 2022-10-15 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0031_alter_imagedata_groupname_alter_imagedata_images_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Researcher",
            fields=[
                (
                    "name",
                    models.CharField(
                        help_text="Researcher's Name",
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Name",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        help_text="Researcher's Avatar",
                        null=True,
                        upload_to="",
                        verbose_name="Avatar",
                    ),
                ),
                (
                    "link",
                    models.URLField(
                        help_text="Researcher's Profile Link on ITS Webiste",
                        null=True,
                        verbose_name="link",
                    ),
                ),
                (
                    "kwargs",
                    models.JSONField(
                        default=dict,
                        help_text="Optional kwargs for Researcher Section",
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="landingpage",
            name="link",
        ),
        migrations.AddField(
            model_name="landingpage",
            name="kwargs",
            field=models.JSONField(
                default=dict,
                help_text="Optional kwargs for Landing Page's Section",
                null=True,
            ),
        ),
    ]
