# Generated by Django 2.2.13 on 2020-11-16 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20201022_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='uni',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='uni_sub',
        ),
    ]