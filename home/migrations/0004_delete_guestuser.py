# Generated by Django 5.0.6 on 2024-06-05 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_guestuser_guestpassword_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='guestUser',
        ),
    ]
