# Generated by Django 2.1.8 on 2019-05-23 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='free_materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('file', models.FileField(upload_to='studymaterials/freematerials')),
                ('belongs_to', models.CharField(choices=[('Science', 'SCINECE'), ('Commerce', 'COMMERCE'), ('Arts', 'ARTS'), ('Above All', 'ABOVE ALL')], default='Above All', max_length=20)),
            ],
        ),
    ]