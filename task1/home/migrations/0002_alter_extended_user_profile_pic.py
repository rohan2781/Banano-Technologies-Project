# Generated by Django 4.0.1 on 2022-03-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extended_user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]