# Generated by Django 3.2.4 on 2021-06-16 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='theme',
            new_name='value',
        ),
    ]
