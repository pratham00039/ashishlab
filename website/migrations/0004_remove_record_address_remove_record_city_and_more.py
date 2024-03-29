# Generated by Django 4.2.6 on 2024-03-01 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_record_tests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='address',
        ),
        migrations.RemoveField(
            model_name='record',
            name='city',
        ),
        migrations.RemoveField(
            model_name='record',
            name='email',
        ),
        migrations.RemoveField(
            model_name='record',
            name='state',
        ),
        migrations.RemoveField(
            model_name='record',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='record',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
