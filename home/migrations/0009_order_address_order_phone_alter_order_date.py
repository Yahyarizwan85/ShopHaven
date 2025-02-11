# Generated by Django 5.1.2 on 2024-12-03 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank='True', default='', max_length=60),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank='True', default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 3, 9, 36, 44, 414140, tzinfo=datetime.timezone.utc)),
        ),
    ]
