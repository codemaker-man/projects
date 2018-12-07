# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 08:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrowseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useragent', models.CharField(default='', max_length=100, verbose_name='用户浏览器agent信息')),
                ('userid', models.CharField(default='', max_length=256, verbose_name='唯一设备ID')),
            ],
            options={
                'verbose_name': '用户浏览信息表',
                'verbose_name_plural': '用户浏览信息表',
                'db_table': 'browseinfo',
            },
        ),
        migrations.CreateModel(
            name='UserIpInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default='', max_length=40, verbose_name='ip 地址')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '用户访问地址信息表',
                'verbose_name_plural': '用户访问地址信息表',
                'db_table': 'useripinfo',
            },
        ),
        migrations.AddField(
            model_name='browseinfo',
            name='userip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanhosts.UserIpInfo'),
        ),
    ]
