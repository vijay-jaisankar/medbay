# Generated by Django 3.1.7 on 2021-02-20 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_doctor_department'),
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Blog',
        ),
    ]
