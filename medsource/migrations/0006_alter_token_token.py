# Generated by Django 3.2.8 on 2021-11-28 02:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('medsource', '0005_auto_20211128_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='Token'),
        ),
    ]
