# Generated by Django 2.2.6 on 2019-10-12 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0002_auto_20191012_1709'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ksiazka',
            new_name='Book',
        ),
    ]
