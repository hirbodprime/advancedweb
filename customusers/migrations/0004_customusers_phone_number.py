# Generated by Django 4.0.4 on 2022-07-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customusers', '0003_remove_customusers_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusers',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]