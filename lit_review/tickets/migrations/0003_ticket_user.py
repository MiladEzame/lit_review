# Generated by Django 4.0.1 on 2022-01-30 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_date_created_alter_user_email_and_more'),
        ('tickets', '0002_ticket_date_created_alter_ticket_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]