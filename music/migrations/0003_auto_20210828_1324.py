# Generated by Django 3.1.4 on 2021-08-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20210821_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.FileField(upload_to='media'),
        ),
    ]
