# Generated by Django 4.2.1 on 2023-06-08 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_feeding_food'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ['-age']},
        ),
    ]
