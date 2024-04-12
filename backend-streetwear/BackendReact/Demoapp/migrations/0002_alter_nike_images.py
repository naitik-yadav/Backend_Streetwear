# Generated by Django 4.2.4 on 2023-08-08 19:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nike',
            name='images',
            field=models.FileField(default='path/to/default/image.png', upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
