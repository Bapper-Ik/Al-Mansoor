# Generated by Django 4.0.6 on 2022-07-06 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_quality_atampa_cotton'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='male',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
