#安装(centos7)
##编译
	yum install -y gcc make
	wget  http://download.redis.io/releases/redis-3.2.6.tar.gz
	tar zxvf  redis-3.2.6.tar.gz
	cd redis-3.2.6
	make
	
##配置
	cd src
	cp redis-server redis-cli redis-sentinel redis-benchmark redis-check-aof  /usr/local/bin

	sysctl -w vm.overcommit_memory=1
	sysctl -w net.core.somaxconn=1024
	echo never > /sys/kernel/mm/transparent_hugepage/enabled

	mkdir /etc/redis
	mkdir -p /var/lib/redis/6379
	cd ../
	cp redis.conf /etc/redis/6379.conf
	vi /etc/redis/6379.conf
	//修改内容
	daemonize yes
	pidfile /var/run/redis_6379.pid
	port 6379
	loglevel notice
	logfile /var/log/redis_6379.log
	dir /var/lib/redis/6379
	bind 0.0.0.0

	开机启动
	cp utils/redis_init_script /etc/init.d/redis_6379
	chmod +x /etc/init.d/redis_6379
	vi /etc/systemd/system/redis_6379.service
	输入内容

		[Unit]
		Description=Redis on port 6379
		[Service]
		Type=forking
		ExecStart=/etc/init.d/redis_6379 start
		ExecStop=/etc/init.d/redis_6379 stop
		[Install]
		WantedBy=multi-user.target
     
    启动 systemctl enable redis_6379.service
    	 systemctl restart redis_6379.services 	


#集群配置
[tutorial](http://www.redis.cn/topics/cluster-tutorial.html)
    yum install -y ruby ruby-devel rubygems rpm-build
    gem install redis
    cd src/
    cp redis-server redis-cli redis-sentinel redis-benchmark redis-check-aof  redis-trib.rb /usr/local/bin

    //节点配置(配置多个)
    mkdir /etc/redis
    mkdir -p /var/lib/redis/7000
	cd ../
	cp redis.conf /etc/redis/7000.conf
	vi /etc/redis/7000.conf
	//修改内容
		daemonize yes
		pidfile /var/run/redis_7000.pid
		port 7000
		loglevel notice
		logfile /var/log/redis_7000.log
		dir /var/lib/redis/7000
		cluster-enabled yes
		cluster-config-file nodes-7000.conf
		cluster-node-timeout 15000
		appendonly yes
		bind 0.0.0.0

	开机启动
	cp utils/redis_init_script /etc/init.d/redis_7000
	chmod +x /etc/init.d/redis_7000
	vi /etc/init.d/redis_7000
	修改端口

	vi /etc/systemd/system/redis_7000.service
	输入内容

[Unit]
Description=Redis on port 7000
[Service]
Type=forking
ExecStart=/etc/init.d/redis_7000 start
ExecStop=/etc/init.d/redis_7000 stop
[Install]
WantedBy=multi-user.target
     
    启动 systemctl enable redis_7000.service
    	 systemctl restart redis_7000.service	

    
    //ip地址需要可非本机访问的
    redis-trib.rb create --replicas 1 192.168.100.101:7000 192.168.100.101:7001 192.168.100.101:7002
    redis-trib.rb create  127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002

    


##删除所有记录命令
flushall