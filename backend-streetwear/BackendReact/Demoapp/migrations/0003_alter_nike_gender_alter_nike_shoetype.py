# Generated by Django 4.2.4 on 2023-08-09 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demoapp', '0002_alter_nike_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nike',
            name='Gender',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='nike',
            name='ShoeType',
            field=models.CharField(max_length=225),
        ),
    ]
