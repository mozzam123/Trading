# Generated by Django 4.2.6 on 2023-11-02 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_user_authuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthUser',
        ),
    ]
