# Generated by Django 3.2.11 on 2022-10-20 23:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSystem', '0003_auto_20221020_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 24, 2, 7, 9, 106816)),
        ),
        migrations.AlterField(
            model_name='applications',
            name='published',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 10, 21, 2, 7, 9, 106816), verbose_name='Дата подачи заявки'),
        ),
    ]
