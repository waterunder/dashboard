# Generated by Django 3.1.7 on 2021-04-04 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200912_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.DeleteModel(
            name='ProductTag',
        ),
    ]
