# Generated by Django 2.2.5 on 2019-10-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20191007_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='ssn',
        ),
        migrations.AddField(
            model_name='note',
            name='uplaoded_by',
            field=models.CharField(default='', max_length=20),
        ),
    ]
