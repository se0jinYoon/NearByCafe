# Generated by Django 4.1.6 on 2023-02-13 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_users_verified_alter_users_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
