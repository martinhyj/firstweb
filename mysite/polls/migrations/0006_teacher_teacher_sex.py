# Generated by Django 2.2.1 on 2021-03-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210307_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_sex',
            field=models.CharField(default='', max_length=10),
        ),
    ]
