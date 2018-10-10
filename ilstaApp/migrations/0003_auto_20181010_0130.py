# Generated by Django 2.1.1 on 2018-10-10 01:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ilstaApp', '0002_auto_20181010_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tipps',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capital',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 1, 30, 15, 1015, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='choice',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 1, 30, 15, 4500, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 1, 30, 14, 999477, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 1, 30, 15, 2861, tzinfo=utc)),
        ),
    ]
