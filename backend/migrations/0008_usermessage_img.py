# Generated by Django 2.2 on 2019-10-23 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20191021_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='img',
            field=models.ImageField(default='', upload_to='HeadPortrait', verbose_name='用户头像'),
        ),
    ]