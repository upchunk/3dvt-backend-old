# Generated by Django 4.1 on 2022-09-05 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_imagedata_mapping_imagedata_imagekey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reconstructiontask',
            name='images',
        ),
        migrations.AlterField(
            model_name='reconstructiontask',
            name='result',
            field=models.ForeignKey(blank=True, help_text='Corresponding Task Result', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.resultdata'),
        ),
    ]
