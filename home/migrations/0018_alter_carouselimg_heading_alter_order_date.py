# Generated by Django 5.1.2 on 2025-02-10 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_carouselimg_heading_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimg',
            name='heading',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 2, 10, 14, 0, 30, 510736)),
        ),
    ]
