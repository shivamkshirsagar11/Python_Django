# Generated by Django 4.0.2 on 2022-02-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEhome', '0003_alter_baseprofile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseprofile',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
