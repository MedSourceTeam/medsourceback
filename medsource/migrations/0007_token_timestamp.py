# Generated by Django 3.2.8 on 2021-11-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medsource', '0006_alter_token_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='timestamp',
            field=models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Timestamp'),
        ),
    ]
