# Generated by Django 2.2.1 on 2021-03-04 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210304_0857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='teaxher_major',
            new_name='teacher_major',
        ),
    ]