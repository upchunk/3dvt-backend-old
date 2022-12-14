# Generated by Django 4.1 on 2022-08-26 18:53

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_intuisi_users_institusi'),
    ]

    operations = [
        migrations.CreateModel(
            name='SegmentationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(blank=True, help_text='Image File to be Processed', null=True, upload_to=api.models.ImageDataset)),
                ('mapping', models.FileField(blank=True, help_text='Mapping file of corresponding image to be processed', null=True, upload_to=api.models.MappingDataset)),
            ],
        ),
        migrations.CreateModel(
            name='SegmentationResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_Images', models.FileField(blank=True, help_text='Segmentation Result', null=True, upload_to=api.models.ResultDataset)),
                ('source', models.ForeignKey(help_text='Corresponding Segmentation Data Source', on_delete=django.db.models.deletion.CASCADE, to='api.segmentationdata')),
            ],
        ),
        migrations.CreateModel(
            name='SegmentationTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, help_text='Task Status', max_length=50, null=True)),
                ('model', models.CharField(blank=True, help_text='Selected Segmentation Model', max_length=50, null=True)),
                ('createdate', models.DateTimeField(auto_now_add=True, help_text='Task Creation Date')),
                ('result', models.ForeignKey(help_text='Corresponding Task Result', on_delete=django.db.models.deletion.CASCADE, to='api.segmentationresult')),
            ],
        ),
        migrations.RemoveField(
            model_name='mappingdata',
            name='image',
        ),
        migrations.RemoveField(
            model_name='resultdata',
            name='source',
        ),
        migrations.RemoveField(
            model_name='resultdata',
            name='user',
        ),
        migrations.RemoveField(
            model_name='taskhistory',
            name='result',
        ),
        migrations.RemoveField(
            model_name='taskhistory',
            name='userid',
        ),
        migrations.AlterField(
            model_name='users',
            name='apikey',
            field=models.CharField(blank=True, help_text='User API Key (Token), generated by django AuthToken', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.ImageField(blank=True, help_text='Avatar of this user', null=True, upload_to=api.models.upload_to),
        ),
        migrations.AlterField(
            model_name='users',
            name='institusi',
            field=models.CharField(blank=True, help_text='Institution of this user', max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='ImageData',
        ),
        migrations.DeleteModel(
            name='MappingData',
        ),
        migrations.DeleteModel(
            name='ResultData',
        ),
        migrations.DeleteModel(
            name='TaskHistory',
        ),
        migrations.AddField(
            model_name='segmentationtask',
            name='userid',
            field=models.ForeignKey(help_text='Corresponding user ID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='segmentationresult',
            name='user',
            field=models.ForeignKey(help_text='Corresponding user ID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='segmentationdata',
            name='user',
            field=models.ForeignKey(help_text='Corresponding user ID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
