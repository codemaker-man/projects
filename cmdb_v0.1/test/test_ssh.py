#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xl on 18-12-9

## 1 pexpect
import pexpect
# ret = pexpect.run(command="ls ", withexitstatus=1) # 同时返回命令是否执行成功
# print(ret)

## 1.1 spawn 子程序
# ssh_k = pexpect.spawn('ssh xl@192.168.199.20 -p 22')
# #print(ssh_k.expect("password:")) # 查看是否有期望的结果返回
# print(ssh_k.expect(['password', pexpect.TIMEOUT, pexpect.EOF])) # 加异常 返回0,1,2 代表对应的结果
# $ 表示是本身，即为普通用户

## 1.2 发送指令 send sendline（结尾补空格） sendcontrol（char）

## 2 paramiko
## 2.1 密码登录
import paramiko
jssh = paramiko.SSHClient()
jssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 自动添加到known_hosts
ret = jssh.connect('192.168.199.20', 22, 'xl', 'HWS@5tgb')
print(ret)

## 2.2 秘钥登录
jssh = paramiko.SSHClient()
jssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 自动添加到known_hosts
key = paramiko.RSAKey.from_private_key_file('/home/xl/conf/id_rsa') # 秘钥登录
jssh.connect('192.168.199.20', 22, pkey=key)
stdin, stdout, stderr = jssh.exec_command('ls /tmp') # 获取结果
print(stdout.read())