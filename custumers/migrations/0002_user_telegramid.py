# Generated by Django 4.0.3 on 2022-03-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custumers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegramid',
            field=models.CharField(default='', max_length=100),
        ),
    ]
