# Generated by Django 3.0 on 2020-06-26 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_english_dic', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EnglishItem',
            new_name='WordItem',
        ),
    ]