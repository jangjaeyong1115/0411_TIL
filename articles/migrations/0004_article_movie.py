# Generated by Django 3.2.18 on 2023-04-11 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20230411_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='movie',
            field=models.CharField(default='', max_length=100),
        ),
    ]
