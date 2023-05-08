# Generated by Django 3.2 on 2023-02-21 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseit', '0005_auto_20230221_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(max_length=10),
        ),
    ]
