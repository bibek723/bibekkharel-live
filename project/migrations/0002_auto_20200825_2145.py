# Generated by Django 3.1 on 2020-08-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='bresume/images/'),
        ),
    ]
