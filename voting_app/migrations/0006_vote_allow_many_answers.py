# Generated by Django 3.0.1 on 2020-01-25 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0005_auto_20200125_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='allow_many_answers',
            field=models.BooleanField(default=0),
        ),
    ]
