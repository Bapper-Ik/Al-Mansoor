# Generated by Django 4.0.6 on 2022-07-06 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_atampa_quality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atampa',
            old_name='quality',
            new_name='cotton',
        ),
    ]