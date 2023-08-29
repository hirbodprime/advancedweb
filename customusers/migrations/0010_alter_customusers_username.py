# Generated by Django 4.0.4 on 2022-07-12 17:51

import customusers.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customusers', '0009_alter_customusers_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='username',
            field=models.CharField(error_messages={'max_length': 'length is not acceptable'}, help_text='200 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=200, validators=[customusers.validators.UnicodeUsernameValidator()], verbose_name='نام کاربری'),
        ),
    ]
