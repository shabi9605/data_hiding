# Generated by Django 3.2.6 on 2022-01-07 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0003_alter_mail_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='receiver',
        ),
    ]