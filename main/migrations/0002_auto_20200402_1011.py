# Generated by Django 3.0.5 on 2020-04-02 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solution',
            old_name='titre',
            new_name='nom',
        ),
    ]
