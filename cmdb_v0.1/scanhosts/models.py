#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class UserIpInfo(models.Model):
    class Meta:
        verbose_name = u'用户访问地址信息表'
        verbose_name_plural = verbose_name
        db_table = 'useripinfo'

    ip = models.CharField(max_length=40,
                          default='',
                          verbose_name=u'ip 地址')
    time = models.DateTimeField(verbose_name=u'更新时间',
                                auto_now=True)


class BrowseInfo(models.Model):
    class Meta:
        verbose_name = u'用户浏览信息表'
        verbose_name_plural =verbose_name
        db_table = 'browseinfo'

    useragent = models.CharField(max_length=200,
                                 default='',
                                 verbose_name=u'用户浏览器agent信息')
    userip= models.ForeignKey('UserIpInfo')