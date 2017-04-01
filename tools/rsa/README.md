Do you want to login other's host without input password?To do as following steps: (Linux to Linux)

First: 
[root@host127 ~]# ssh-keygen -t rsa 
this command will generating public/private rsa key pair. 
Your identification has been saved in /root/.ssh/id_rsa
Your public key has been saved in /root/.ssh/id_rsa.pub


second:
[root@host127 ~]# scp /root/.ssh/id_rsa.pub root@192.168.10.184:/root 
[root@host127 ~]# ssh 192.168.10.184 
[root@abc ~]# cat /root/id_rsa.pub >> /root/.ssh/authorized_keys 

ok,you will login 192.168.10.184 without input password.

If you want to login remote linux server with putty work in your local windows, you could do as: (Window to Linux)

1)First, use ssh-kengen to creat public/private rsa key pair.
2)Then, [root@localhost .ssh]# cat id_rsa.pub > authorized_keys

3)Download the private key with winSCP, and then use puttygen to convert the private key to the format which linux could accept.

4)Set putty, and load the new pricate key.

Now, you could loing remote linux server without input password.