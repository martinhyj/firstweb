# Generated by Django 2.2.1 on 2021-03-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210304_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='APIKEY',
            field=models.CharField(default='abcdefghijklmn', max_length=30, verbose_name='APIkey'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_age',
            field=models.IntegerField(default=0),
        ),
    ]
