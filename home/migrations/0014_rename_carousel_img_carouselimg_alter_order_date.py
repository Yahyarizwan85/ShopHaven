# Generated by Django 5.1.2 on 2025-01-16 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_carousel_img_alter_order_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='carousel_img',
            new_name='CarouselImg',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 1, 16, 19, 52, 33, 680743)),
        ),
    ]
