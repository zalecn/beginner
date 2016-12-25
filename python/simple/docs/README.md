#Python备忘录
[TOC]

##工具篇
###WEB框架

####FLASK
#####安装
[官方中文文档](http://docs.jinkan.org/docs/flask/installation.html)
前置条件需要安装Python和Pip，然后执行下面命令：

	pip install falsk


**备注**

* 编码异常
>在windows安装过程中可能出现编码异常，需要在python目录Lib\site-packages下添加sitecustomize.py文件
	内容如下：
>		
>		import sys 
>		sys.setdefaultencoding('utf8')  

###杂项
####Pip安装
[下载Pip安装包](https://pypi.python.org/pypi/pip#downloads)
选择pip-8.1.2.tar.gz (md5, pgp)
下载完成并解压后执行

	python setup.py install
>	源
>	豆瓣：http://pypi.douban.com/simple/
>	清华：https://pypi.tuna.tsinghua.edu.cn/simple
>	临时使用：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gevent
>	永久修改：
>		 Linux:
>			修改 ~/.pip/pip.conf (没有就创建一个)， 修改 index-url至tuna，内容如下：
>			[global]
>			index-url = https://pypi.tuna.tsinghua.edu.cn/simple
>		windows:
>			直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下
>			[global]
>			index-url = https://pypi.tuna.tsinghua.edu.cn/simple

####Api本地文档
执行以下命令，在浏览器中查看API，地址为:http://127.0.0.1:1234

	python -m pydoc -p 1234
	
####gevent安装
windows上需要python2.7.5以上，不然运行会遇到dll为找到
####依赖包管理
使用pip导出依赖

	pip freeze > requirements.pf
	
安装依赖

	pip install -r requirements.pf

####sqlautocode
> ImportError: cannot import name _deferred_relation
[issues](https://github.com/dgleba/sqlautocode/issues/42)
[sa-0.8-fixes.diff](https://storage.googleapis.com/google-code-attachments/sqlautocode/issue-42/comment-1/sa-0.8-fixes.diff)

##语法篇
###中文

* 使用UTF8编码
> 在代码最前面添加以下代码
> 
> 		# -*- coding: utf8 -*-
> 		from __future__ import unicode_literals


###syslog
	import logging
	from logging.handlers import SysLogHandler

	handler = SysLogHandler(address = '/dev/log', facility=SysLogHandler.LOG_DAEMON)
	my_logger = logging.getLogger('MyLogger')
	my_logger.setLevel(logging.DEBUG)
	my_logger.addHandler(handler)
	my_logger.error('11111111111111111111')

其中address必须设置
可以通过facility来指定最终日志存储在哪个文件
设置facility=SysLogHandler.LOG_LOCAL0
在Ubuntu下 在文件中/etc/rsyslog.d/50-default.conf 添加
local0.*                        -/var/log/my.log


