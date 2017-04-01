#配置
[参考](http://www.linuxidc.com/Linux/2016-03/128880.htm)
##mariadb
yum install mariadb mariadb-server
systemctl enable mariadb-server
systemctl restart mariadb-server

	mysql_secure_installation
	首先是设置密码，会提示先输入密码

	Enter current password for root (enter for none):<–初次运行直接回车

	设置密码

	Set root password? [Y/n] <– 是否设置root用户密码，输入y并回车或直接回车
	New password: <– 设置root用户的密码
	Re-enter new password: <– 再输入一次你设置的密码

	其他配置

	Remove anonymous users? [Y/n] <– 是否删除匿名用户，回车

	Disallow root login remotely? [Y/n] <–是否禁止root远程登录,回车,

	Remove test database and access to it? [Y/n] <– 是否删除test数据库，回车

	Reload privilege tables now? [Y/n] <– 是否重新加载权限表，回车

	初始化MariaDB完成，接下来测试登录

	mysql -uroot -ppassword
	完成。

##添加用户，设置权限
创建用户命令

mysql>create user username@localhost identified by 'password';
直接创建用户并授权的命令

mysql>grant all on *.* to username@localhost indentified by 'password';
授予外网登陆权限 

mysql>grant all privileges on *.* to username@'%' identified by 'password';
授予权限并且可以授权

mysql>grant all privileges on *.* to username@'hostname' identified by 'password' with grant option;

刷新权限
mysql>flush privileges;


##连接数
	mysql>show variables like 'max_connections';(查可以看当前的最大连接数)
	msyql>set global max_connections=1000;(设置最大连接数为1000，可以再次查看是否设置成功)

	或修改配置文件/etc/my.cnf
	max_connections=100000