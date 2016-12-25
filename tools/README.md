#sublime3

##安装包管理器
执行快捷键 ctrl+`，并在窗口中执行以下代码

	import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())

##激活码
	Michael Barnes
	Single User License
	EA7E-821385
	8A353C41 872A0D5C DF9B2950 AFF6F667
	C458EA6D 8EA3C286 98D1D650 131A97AB
	AA919AEC EF20E143 B361B1E7 4C8B7F04
	B085E65E 2F5F5360 8489D422 FB8FC1AA
	93F6323C FD7F7544 3F39C318 D95E6480
	FCCC7561 8A4A1741 68FA4223 ADCEDE07
	200C25BE DBBC4855 C4CFB774 C5EC138C
	0FEC1CEF D9DCECEC D3A5DAD1 01316C36

##汉化插件
   快捷键ctrl+shift+p  输入install package
   输入chineseLocalization 安装该插件

##markdown插件
###MarkdownEditing
修改配置文件 
Package Setting -> Markdown Editing -> Markdown GFM Settings - User

	{
    "extensions":
    [
        "md"
    ],
    "tab_size": 4,
    "draw_centered": false,
    "color_scheme": "Packages/MarkdownEditing/MarkdownEditor-Dark.tmTheme",
    "line_numbers": true,
	}

###MarkdownPreview
ctrl + b 生成html  

###颜色配置
Markdown extend 
Monokai Extended
> 注意需要将 Markdown 的文件格式与 Markdown Extended 这种语法关联起来，做法是点击 Sublime 右下角文档格式，在列表最上方名为 Open all with current extension as 二级列表中选择 Markdown Extended。

##GO插件
gosublime

##安装插件过程中以下错误
	There are no packages available for installation
解决方法：
package-setting -> package-control -> setting-user
删除文件内容


##Loading Pyv8 binary, please wait
[github下载](https://github.com/emmetio/pyv8-binaries)