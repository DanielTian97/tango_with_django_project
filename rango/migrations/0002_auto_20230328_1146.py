# Generated by Django 2.1.5 on 2023-03-28 10:46

from django.db import migrations, models
import rango.models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='liked_categories',
            field=models.ManyToManyField(to='rango.Category'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to=rango.models.UserProfile.image_path),
        ),
    ]
