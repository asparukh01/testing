# Generated by Django 4.0.6 on 2022-07-12 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0004_employee_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
    ]
