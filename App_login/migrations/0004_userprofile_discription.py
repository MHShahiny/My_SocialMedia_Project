# Generated by Django 5.0.4 on 2024-05-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_login', '0003_userprofile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='discription',
            field=models.TextField(blank=True),
        ),
    ]
