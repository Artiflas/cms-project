# Generated by Django 3.0.7 on 2020-12-01 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20201130_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='create_date',
            new_name='erstellungsdatum',
        ),
    ]
