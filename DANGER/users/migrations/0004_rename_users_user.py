# Generated by Django 4.0.3 on 2022-03-17 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_name_users_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='User',
        ),
    ]