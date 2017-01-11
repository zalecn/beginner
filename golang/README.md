#vendor
go get -u -v github.com/kardianos/govendor
govendor init
govendor add +external

#protocol
[git](https://github.com/golang/protobuf)
[protoc3文档](https://developers.google.com/protocol-buffers/docs/proto3#packages)


##安装
	go get -u -v github.com/golang/protobuf/proto
	go get -u -v github.com/golang/protobuf/protoc-gen-go

	The compiler plugin, protoc-gen-go, will be installed in $GOBIN, defaulting to $GOPATH/bin. 
	It must be in your $PATH for the protocol compiler, protoc, to find it.

	[下载protoc](https://github.com/google/protobuf/releases) 到对应bin目录

#sublime 开发环境
安装GoSublime创建
配置GOPATH，GOROOT
Preferences -> package settings -> GoSublime -> Settings - Uesrs
	{
	    "env": {
	        "GOPATH": "F:/mygo",
	        "GOROOT": "E:/Go"
	    }
	}