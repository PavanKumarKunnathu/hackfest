# Generated by Django 4.0 on 2022-01-12 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_doctors_delete_demotable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='doctors',
            name='email',
        ),
        migrations.AddField(
            model_name='doctors',
            name='gender',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='doctors',
            name='password',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='doctors',
            name='phone',
            field=models.TextField(default='', max_length=200, unique=True),
        ),
    ]
