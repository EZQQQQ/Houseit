# Generated by Django 4.1.7 on 2023-04-02 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseit', '0009_listedproperty_user_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userbookmarks',
            fields=[
                ('userid', models.IntegerField(blank=True, db_column='userID', null=True)),
                ('propertyid', models.AutoField(db_column='propertyID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'UserBookmarks',
                'managed': False,
            },
        ),
    ]