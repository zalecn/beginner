#npm
Nodejs 6.3.0版本之后会自带npm的包管理所以不需要单独的安装npm
##更换npm库的源
	npm config set registry https://registry.npm.taobao.org

	npm install -g cnpm --registry=https://registry.npm.taobao.org

##centos7 install nodejs
###编译好的文件
	wget http://nodejs.org/dist/v6.9.2/node-v6.9.2-linux-x64.tar.gz
	ln -s /home/zale/node-v6.9.2-linux-x64/bin/node /usr/local/bin/node
	ln -s /home/zale/node-v6.9.2-linux-x64/bin/npm /usr/local/bin/npm

###源文件安装 

1.安装环境
	sudo yum install gcc gcc-c++
2.下载源代码
	wget https://nodejs.org/dist/v6.9.2/node-v6.9.2.tar.gz
3.解压
	tar xvf node-v6.9.2-linux-x64.tar.xz
4.安装
	cd node-v*
	./configure
	make
	sudo make install
	node --version

##heapdump
###问题

	windows:
	error MSB8036: The Windows SDK version 8.1 was not found
	安装 Windows SDK 8.1

