# Generated by Django 2.2.1 on 2019-05-07 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190507_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 7, 11, 0, 43, 948721)),
        ),
    ]