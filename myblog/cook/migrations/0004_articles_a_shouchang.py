# Generated by Django 2.0 on 2018-01-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0003_auto_20180110_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='a_shouchang',
            field=models.IntegerField(default=0),
        ),
    ]
