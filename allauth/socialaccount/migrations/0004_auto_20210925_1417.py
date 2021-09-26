# Generated by Django 2.2 on 2021-09-25 14:17

from django.db import migrations
from .. import app_settings

class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialaccount',
            name='tag',
            field=app_settings.build_social_account_model_tag_field(),
        ),
        migrations.AlterUniqueTogether(
            name='socialaccount',
            unique_together={('provider', 'uid', 'tag')},
        ),
    ]
