# Generated by Django 4.1.2 on 2022-10-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0028_landingpage"),
    ]

    operations = [
        migrations.AddField(
            model_name="landingpage",
            name="section_title",
            field=models.CharField(
                default=str,
                help_text="Landing Page's Section Title",
                max_length=50,
                verbose_name="title",
            ),
        ),
    ]
