# Generated by Django 2.2.6 on 2019-10-12 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0010_auto_20191012_2014'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
