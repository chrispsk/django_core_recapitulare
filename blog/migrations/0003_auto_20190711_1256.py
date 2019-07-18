# Generated by Django 2.2.3 on 2019-07-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190711_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(error_messages={'blank': 'This field is not full, please try again.', 'unique': 'This title is not unique, please try again.'}, help_text='Must be a unique title.', max_length=240, unique=True, verbose_name='Post title'),
        ),
    ]