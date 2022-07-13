# Generated by Django 4.0.4 on 2022-07-12 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customusers',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='customusers',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
