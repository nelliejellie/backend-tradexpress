# Generated by Django 3.2.8 on 2021-10-15 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='type_of_account',
        ),
        migrations.AddField(
            model_name='user',
            name='business',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='individual',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]