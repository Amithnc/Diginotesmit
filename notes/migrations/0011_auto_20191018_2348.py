# Generated by Django 2.2.5 on 2019-10-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_remove_note_uploaded_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='branch_semid',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='note',
            name='added_by',
            field=models.CharField(default='', help_text='type your username', max_length=10),
        ),
        migrations.AlterField(
            model_name='note',
            name='module_no',
            field=models.CharField(default='', help_text='please choose the module number', max_length=1),
        ),
        migrations.AlterField(
            model_name='note',
            name='upload_file',
            field=models.FileField(help_text='upload the correct file    NOTE:U CANT CHANGE AFTER UPLOADING', upload_to='files/'),
        ),
    ]
