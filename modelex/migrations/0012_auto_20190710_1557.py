# Generated by Django 2.2.3 on 2019-07-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelex', '0011_auto_20190710_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
