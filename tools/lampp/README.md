# appache vhost配置
## httpd.conf【主配置文件】
1.加入这两个模块让apache支持代理
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so
2.开启（lampp此步骤省略）
NameVirtualHost *:80
3.include配置文件（lampp此步骤省略）
Include \etc\httpd-vhost.conf
## httpd-vhost.conf【我们代理所在配置文件】
<VirtualHost *:80>
    DocumentRoot "F:/feet/htdocs"
    ServerName localhost
</VirtualHost>
<VirtualHost *:80>
    ServerName a.b.com
    ProxyPass / http://10.10.10.251:11180/
    ProxyPassReverse / http://10.10.10.251:11180/
</VirtualHost>
<VirtualHost *:80>
    ServerName a.b.com
    ProxyPass /test http://10.10.10.251:11180/
    ProxyPassReverse /test http://10.10.10.251:11180/
</VirtualHost>

