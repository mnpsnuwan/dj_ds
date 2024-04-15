# Generated by Django 5.0.4 on 2024-04-15 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(default='no_picture.png', upload_to='products')),
                ('price', models.FloatField(help_text='in US dollers $')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('upated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
