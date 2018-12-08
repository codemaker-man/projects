# -*- coding: utf-8 -*-
#!/usr/bin/python
#########################################################################

import pexpect

def login_ssh_passwd(port="",user="",host="",passwd=""):
    '''函数：用于实现pexepect实现ssh的自动化用户密码登录'''

    # print 'ssh -p %s %s@%s' % (port,user, host)
    if  port and user and host and passwd:
        ssh = pexpect.spawn('ssh -p %s %s@%s' % (port, user, host))
        # continue connecting (yes/no)? 表示第一次登录服务器
        # 加入到～/.ssh/known_hosts 防止中间人攻击
        i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5)
        if i == 0 :
            ssh.sendline(passwd)
        elif i == 1:
            ssh.sendline('yes\n')
            ssh.expect('password: ')
            ssh.sendline(passwd)
        # 用root用户登录，成功后$变为#
        index = ssh.expect (["#", pexpect.EOF, pexpect.TIMEOUT])

        if index == 0:
            print ("logging in as root!")
            ssh.interact()
        elif index == 1:
            print ("logging process exit!")
        elif index == 2:
            print ("logging timeout exit")
    else:
        print ("Parameter error!")

def login_ssh_key(keyfile="",user="",host="",port=""):
    '''函数：用于实现pexepect实现ssh的自动化密钥登录'''

    if  port and user and host and keyfile:
        ssh = pexpect.spawn('ssh -i %s -p %s %s@%s' % (keyfile,port,user, host))
        i = ssh.expect( [pexpect.TIMEOUT,'continue connecting (yes/no)?'], timeout=2)
        # print '...................................',0
        if i == 1:
            ssh.sendline('yes\n')
            index = ssh.expect (["#", pexpect.EOF, pexpect.TIMEOUT])
        else:
            index = ssh.expect (["#", pexpect.EOF, pexpect.TIMEOUT])
        if index == 0:
            print ("logging in as root!")
            ssh.interact()
        elif index == 1:
            print ("logging process exit!")
        elif index == 2:
            print ("logging timeout exit")
    else:
        print ("Parameter error!")

def main():
    '''主函数：实现两种方式分别的登录'''
    # login_ssh_passwd(port='22',user='root',host='192.168.1.101',passwd='imooccs')
    login_ssh_key(keyfile="/tmp/id_rsa",port='22',user='root',host='192.168.1.101')


if __name__ == "__main__":
    main()
