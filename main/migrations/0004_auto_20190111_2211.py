# Generated by Django 2.0 on 2019-01-11 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='text',
        ),
    ]
