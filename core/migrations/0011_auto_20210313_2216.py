# Generated by Django 3.1.7 on 2021-03-13 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_bulletins_recurring'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bulletins',
            new_name='BulletinSubscriber',
        ),
    ]
