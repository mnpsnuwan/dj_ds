# Generated by Django 5.0.4 on 2024-04-15 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('profiles', '0001_initial'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sales',
            new_name='Sale',
        ),
    ]