# Generated by Django 4.0.1 on 2022-01-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_remove_physician_clinic_address_remove_physician_dob_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='demophy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='physician',
        ),
    ]
