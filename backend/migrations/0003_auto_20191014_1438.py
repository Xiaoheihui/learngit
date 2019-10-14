# Generated by Django 2.2.4 on 2019-10-14 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20191008_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprecord',
            name='RPromulgatorID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Promulgator_set', to=settings.AUTH_USER_MODEL, verbose_name='发布者编号'),
        ),
        migrations.AlterField(
            model_name='markmessage',
            name='MarkTime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='收藏时间'),
        ),
    ]
