# Generated by Django 3.2.8 on 2021-11-28 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medsource', '0007_token_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='timestamp',
        ),
    ]