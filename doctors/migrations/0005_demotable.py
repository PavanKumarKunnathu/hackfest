# Generated by Django 4.0 on 2022-01-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_demophy_delete_physician'),
    ]

    operations = [
        migrations.CreateModel(
            name='demotable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specility', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('clinic_address', models.TextField()),
                ('dob', models.DateField()),
                ('reg_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
