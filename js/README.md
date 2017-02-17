#JS
##ES6
###资料
[ECMAScript 6 入门](http://es6.ruanyifeng.com/#docs/string)
[多语言转换 i18n]

##protocol
[git](https://github.com/google/protobuf/tree/master/js)
[protoc3文档](https://developers.google.com/protocol-buffers/docs/proto3#packages)


###使用
[download a pre-built binary](https://github.com/google/protobuf/releases)

	To use Protocol Buffers with JavaScript, you need two main components:
	1.The protobuf runtime library. You can install this with npm install google-protobuf, or use the files in this directory.
	2.The Protocol Compiler protoc. This translates .proto files into .js files. The compiler is not currently available via npm, but you can download a pre-built binary on GitHub (look for the protoc-*.zip files under Downloads).

	

	protoc --js_out=library=myproto_libs,binary:. messages.proto base.proto
	protoc --js_out=import_style=commonjs,binary:. messages.proto base.proto




##WebSocket
###问题
1. failed: Connection closed before receiving a handshake response
	有可能本机开启了代理，关闭代理试试。
2. 
