# Generated by Django 4.2.1 on 2023-06-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_sleeping_moving_loving_cleaning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moving',
            name='move',
            field=models.CharField(choices=[('move1', 'play fetch'), ('move2', 'go for a walk')], default='move1', max_length=6),
        ),
    ]
