# Generated by Django 4.0.1 on 2022-01-27 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_date_created_alter_user_email_and_more'),
        ('userfollows', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserFollows',
            new_name='UserFollow',
        ),
    ]