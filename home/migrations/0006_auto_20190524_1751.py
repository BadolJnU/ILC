# Generated by Django 2.1.8 on 2019-05-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
