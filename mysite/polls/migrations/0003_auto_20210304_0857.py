# Generated by Django 2.2.1 on 2021-03-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_age',
            field=models.IntegerField(),
        ),
    ]