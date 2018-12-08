#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xl on 18-12-9

import yaml

f = open('conf/scanhosts.yaml','r',encoding='utf-8')
a= yaml.load(f.read())
print(a)