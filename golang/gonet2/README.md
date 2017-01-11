#安装

##docker 
###镜像加速
	https://www.daocloud.io/mirror#accelerator-doc

	curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://ce29fac1.m.daocloud.io
###windows

	[下载](https://www.docker.com/)
	WINDOWS需要win10或使用vbox

###Linux
	sudo yum update

	sudo tee /etc/yum.repos.d/docker.repo <<-'EOF'
	[dockerrepo]
	name=Docker Repository
	baseurl=https://yum.dockerproject.org/repo/main/centos/7/
	enabled=1
	gpgcheck=1
	gpgkey=https://yum.dockerproject.org/gpg
	EOF

	sudo yum install docker-engine

	sudo systemctl enable docker.service

	sudo systemctl start docker
###工具
1.etcd
	docker pull quay.io/coreos/etcd:v2.0.3
	#docker pull quay.io/coreos/etcd
	[etcd](https://coreos.com/etcd/docs/2.0.8/docker_guide.html#running-etcd-in-standalone-mode)

	docker run -d -p 4001:4001 -p 2380:2380 -p 2379:2379 --name etcd quay.io/coreos/etcd:v2.0.3 \
	 -name etcd0 \
	 -advertise-client-urls http://${HostIP}:2379,http://${HostIP}:4001 \
	 -listen-client-urls http://0.0.0.0:2379,http://0.0.0.0:4001 \
	 -initial-advertise-peer-urls http://${HostIP}:2380 \
	 -listen-peer-urls http://0.0.0.0:2380 \
	 -initial-cluster-token etcd-cluster-1 \
	 -initial-cluster etcd0=http://${HostIP}:2380 \
	 -initial-cluster-state new

2.etcd-browser
	docker pull buddho/etcd-browser
	[etcd-browser](https://hub.docker.com/r/buddho/etcd-browser/)

	sudo docker run -d --name etcd-browser -p 0.0.0.0:8000:8000 --env ETCD_HOST=192.168.100.101 --env AUTH_PASS=doe buddho/etcd-browser

3.mongo
	docker pull mongo
	[mongo](https://hub.docker.com/_/mongo/)

4.StatsD + Graphite + Grafana 2 + Kamon Dashboards
	docker pull kamon/grafana_graphite
	[grafana_graphite](https://hub.docker.com/r/kamon/grafana_graphite/)

	docker run -d -p 80:80 -p 8125:8125/udp -p 8126:8126 --name kamon-grafana-dashboard kamon/grafana_graphite

5.Elasticsearch, Logstash, Kibana (ELK) Docker image
	docker pull sebp/elk
	[elk-docker](http://elk-docker.readthedocs.io/)
	sudo docker run -d -p 5601:5601 -p 9200:9200 -p 5044:5044 --name elk sebp/elk

6.logspout
	docker pull gliderlabs/logspout
	[logspout](https://hub.docker.com/r/gliderlabs/logspout/)

7.registrator
	docker pull gliderlabs/registrator
	[registrator](https://hub.docker.com/r/gliderlabs/registrator/)




###源代码
	git clone https://github.com/gonet2/agent.git
	git clone https://github.com/gonet2/game.git
	git clone https://github.com/gonet2/snowflake.git
	git clone https://github.com/gonet2/chat.git
	git clone https://github.com/gonet2/rank.git
	git clone https://github.com/gonet2/geoip.git
	git clone https://github.com/gonet2/archiver.git
	git clone https://github.com/gonet2/wordfilter.git
	git clone https://github.com/gonet2/tools.git