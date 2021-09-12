# Generated by Django 3.2 on 2021-09-12 02:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210912_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectdetectionsample',
            name='image_url',
            field=models.CharField(max_length=355),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 9, 12, 2, 41, 1, 729361, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='header_image_url',
            field=models.CharField(default='https://neurohive.io/wp-content/uploads/2019/01/dd-e1547642312239.jpg', max_length=355),
        ),
    ]
