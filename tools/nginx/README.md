#windows上安装
[下载](http://nginx.org/en/download.html)后解压，
命令

	start nginx.exe     //启动nginx
	nginx.exe -s stop   //停止nginx
	nginx.exe -s reload //重新加载nginx
	nginx.exe -s quit   //退出nginx

#参考文档
[tengine](http://tengine.taobao.org/book/index.html)


#centos7
##安装
添加源
rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
安装
yum install nginx

##配置
配置文件位置在/etc/nginx/

##设置启动
systemctl enable nginx
systemctl restart nginx

##目录
一般目录放在/usr/shared/nginx/下， 其他路径下需要解决权限问题。



###禁用缓存

location ~ .*/\.(css|js)$ {
    add_header Cache-Control 'no-store';
}


###bind() to 0.0.0.0:8001 failed (13: Permission denied)
[地址](https://my.oschina.net/aibati2008/blog/729674)
This will most likely be related to SELinux

semanage port -l | grep http_port_t
http_port_t                    tcp      80, 81, 443, 488, 8008, 8009, 8443, 9000
As you can see from the output above with SELinux in enforcing mode http is only allowed to bind to the listed ports. The solution is to add the ports you want to bind on to the list

semanage port -a -t http_port_t  -p tcp 8090
will add port 8090 to the list.


###Resource interpreted as Stylesheet but transferred with MIME type text/plain
需要添加  包含mime.types文件
include       /etc/nginx/mime.types;