# Generated by Django 4.0.1 on 2022-03-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_extended_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extended_user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/core/profile'),
        ),
    ]
