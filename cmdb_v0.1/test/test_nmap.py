#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xl on 18-12-9

import nmap
import telnetlib
nm = nmap.PortScanner()
ret = nm.scan(hosts="192.168.199.0/24", arguments="-n -sP -PE") # 扫描目标网段
print(ret)
print(nm.all_hosts())  # 查看局域网中的主机 exp：['192.168.199.1' ...]

#
# te = telnetlib.Telnet(host='192.168.199.1', port='22', timeout=3)
# t_ret = te.read_until(b'\n') # 结果出现\n结束
# print(t_ret.decode()) # SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.6
#
# import re
# pattern = re.search('SSH', t_ret.decode())
# # 查看活动主机的22端口是否为SSH使用
# print(pattern) # <_sre.SRE_Match object; span=(0, 3), match='SSH'>
#                # or None