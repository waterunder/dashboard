# Generated by Django 3.0.8 on 2020-07-23 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='country',
            field=models.CharField(choices=[('uk', 'United Kingdom'), ('us', 'United States of America'), ('ar', 'Argentina')], max_length=3),
        ),
    ]
